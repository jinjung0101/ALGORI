# solver_intervals.py
# Python 3.10+, 외부 패키지: requests
# import sys
# import requests
# from dataclasses import dataclass
# from bisect import bisect_left
# from typing import List, Tuple, Dict, Optional

import sys
import requests
from dataclasses import dataclass


BASE = "https://7zszxecwra.execute-api.ap-northeast-2.amazonaws.com/api"
X_AUTH_TOKEN = "1851f013ecd376874e539f4b"

@dataclass
class Req:
    id: int
    amount: int
    check_in: int
    check_out: int
    req_day: int
    deadline: int
    weight: float

@dataclass
class Plan:
    floor: int
    start_pos: int
    amount: int
    check_in: int
    check_out: int

class API:
    def __init__(self, problem: int):
        self.problem = problem
        self.auth = None

    def start(self) -> Dict:
        r = requests.post(
            f"{BASE}/start",
            headers={"X-Auth-Token": X_AUTH_TOKEN, "Content-Type": "application/json"},
            json={"problem": self.problem},
            timeout=10,
        )
        r.raise_for_status()
        data = r.json()
        self.auth = data["auth_key"]
        return data

    def new_requests(self) -> Dict:
        r = requests.get(
            f"{BASE}/new_requests",
            headers={"Authorization": self.auth, "Content-Type": "application/json"},
            timeout=10,
        )
        r.raise_for_status()
        return r.json()

    def reply(self, replies: List[Dict]) -> Dict:
        r = requests.put(
            f"{BASE}/reply",
            headers={"Authorization": self.auth, "Content-Type": "application/json"},
            json={"replies": replies},
            timeout=10,
        )
        r.raise_for_status()
        return r.json()

    def simulate(self, assigns: List[Dict]) -> Dict:
        r = requests.put(
            f"{BASE}/simulate",
            headers={"Authorization": self.auth, "Content-Type": "application/json"},
            json={"room_assign": assigns},
            timeout=10,
        )
        r.raise_for_status()
        return r.json()

    def score(self) -> Dict:
        r = requests.get(
            f"{BASE}/score",
            headers={"Authorization": self.auth, "Content-Type": "application/json"},
            timeout=10,
        )
        r.raise_for_status()
        return r.json()

class SlotCalendar:
    """
    하나의 방(층+위치)의 점유 구간을 관리하는 캘린더.
    intervals: [(s,e), ...], e <= 다음 s 보장 (비중첩·정렬).
    """
    def __init__(self):
        self.intervals: List[Tuple[int,int]] = []
        self.starts: List[int] = []

    def is_free(self, s: int, e: int) -> bool:
        """구간 [s,e) 이 기존 점유와 겹치지 않으면 True"""
        idx = bisect_left(self.starts, s)
        # 이전 구간과 겹침?
        if idx > 0:
            ps, pe = self.intervals[idx-1]
            if ps < e and s < pe:
                return False
        # 현재(혹은 다음) 구간과 겹침?
        if idx < len(self.intervals):
            cs, ce = self.intervals[idx]
            if cs < e and s < ce:
                return False
        return True

    def add(self, s: int, e: int) -> None:
        """[s,e) 삽입 (겹치지 않는다고 가정)"""
        idx = bisect_left(self.starts, s)
        self.intervals.insert(idx, (s,e))
        self.starts.insert(idx, s)

class Solver:
    def __init__(self, problem: int):
        self.problem = problem
        if problem == 1:
            self.H, self.W, self.MAX_DAY, self.TARGET = 3, 20, 200, 60
        else:
            self.H, self.W, self.MAX_DAY, self.TARGET = 10, 200, 1000, 75

        # booked[floor][pos] => SlotCalendar
        self.booked: List[List[SlotCalendar]] = [
            [SlotCalendar() for _ in range(self.W + 1)]
            for _ in range(self.H + 1)
        ]

        self.pending: Dict[int, Req] = {}
        self.plans: Dict[int, Plan] = {}
        self.answered: set[int] = set()

        self.api = API(problem)

    def weight_of(self, amount: int, duration: int, ci: int) -> float:
        w = amount * duration
        if self.problem == 2:
            if amount >= 13 and 7 <= duration <= 30:
                w *= 1.15  # 대형·중기 체류 약한 보너스
        return float(w)

    def can_place_on_floor(self, f: int, start_pos: int, k: int, s: int, e: int) -> bool:
        """층 f, 시작 start_pos에서 길이 k 연속 포지션이 [s,e) 모두 비어있는지"""
        end_pos = start_pos + k - 1
        for pos in range(start_pos, end_pos + 1):
            if not self.booked[f][pos].is_free(s, e):
                return False
        return True

    def place_on_floor(self, f: int, start_pos: int, k: int, s: int, e: int) -> None:
        """실제 삽입 (자원 고정)"""
        end_pos = start_pos + k - 1
        for pos in range(start_pos, end_pos + 1):
            self.booked[f][pos].add(s, e)

    def place_request(self, r: Req) -> Optional[Tuple[int,int]]:
        """요청 r을 사전 배치. 가능하면 (floor, start_pos) 반환"""
        s, e, k = r.check_in, r.check_out, r.amount
        last_start = self.W - k + 1
        for f in range(1, self.H + 1):
            # 왼쪽부터 탐색(번호 작은 구간 선호)
            for start_pos in range(1, last_start + 1):
                if self.can_place_on_floor(f, start_pos, k, s, e):
                    self.place_on_floor(f, start_pos, k, s, e)
                    return (f, start_pos)
        return None

    def run(self):
        start = self.api.start()
        day = start["day"]

        while day <= self.MAX_DAY:
            # 1) 오늘 들어온 요청 적재
            nr = self.api.new_requests()
            for v in nr.get("reservations_info", []):
                amount = int(v["amount"])
                ci = int(v["check_in_date"])
                co = int(v["check_out_date"])
                dur = co - ci
                req = Req(
                    id=int(v["id"]),
                    amount=amount,
                    check_in=ci,
                    check_out=co,
                    req_day=day,
                    deadline=min(day + 14, ci - 1),
                    weight=self.weight_of(amount, dur, ci),
                )
                self.pending[req.id] = req

            replies = []

            # 2) 오늘 데드라인 우선 처리
            must = [r for r in self.pending.values() if r.deadline == day]
            must.sort(key=lambda r: (r.check_in, -r.weight))
            for r in must:
                placed = self.place_request(r)
                if placed:
                    f, sp = placed
                    self.plans[r.id] = Plan(f, sp, r.amount, r.check_in, r.check_out)
                    replies.append({"id": r.id, "reply": "accepted"})
                else:
                    replies.append({"id": r.id, "reply": "refused"})
                self.answered.add(r.id)
                self.pending.pop(r.id, None)

            # 3) 나머지 중 배치 가능한 건 즉시 승낙(효율성 점수↑)
            cand = [r for r in self.pending.values() if r.id not in self.answered]
            cand.sort(key=lambda r: (r.check_in, -r.weight, -r.amount, r.deadline))
            for r in cand:
                placed = self.place_request(r)
                if placed:
                    f, sp = placed
                    self.plans[r.id] = Plan(f, sp, r.amount, r.check_in, r.check_out)
                    replies.append({"id": r.id, "reply": "accepted"})
                    self.answered.add(r.id)
                    self.pending.pop(r.id, None)

            if replies:
                self.api.reply(replies)

            # 4) 오늘 체크인 배정(사전 계획 기반)
            assigns = []
            for rid, p in self.plans.items():
                if p.check_in == day:
                    room_number = p.floor * 1000 + p.start_pos
                    assigns.append({"id": rid, "room_number": room_number})

            sim = self.api.simulate(assigns)
            day = sim["day"]

        sc = self.api.score()
        print(
            f"accuracy={sc.get('accuracy_score'):.2f}, "
            f"efficiency={sc.get('efficiency_score'):.2f}, "
            f"penalty={sc.get('penalty_score'):.2f}, "
            f"score={sc.get('score'):.2f}"
        )

def main():
    problem = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    Solver(problem).run()

if __name__ == "__main__":
    main()
