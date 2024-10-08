import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    kg, cm = map(int, input().split())
    arr.append((kg, cm))

for i in range(n):
    temp = 1
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            temp += 1
    print(temp, end=' ')





# 다른 풀이 -----------------------------------------------
# 각 개인의 정보를 객체나 딕셔너리로 관리하여, 코드의 가독성과 유지 관리를 용이하게 합니다.
# 등수 계산 로직을 분리하여, 함수를 통해 구현함으로써 코드를 모듈화합니다.

input = sys.stdin.readline

def calculate_rank(people):
    n = len(people)
    ranks = [1] * n  # 모든 사람의 초기 등수는 1로 시작

    for i in range(n):
        for j in range(n):
            if people[i]['kg'] < people[j]['kg'] and people[i]['cm'] < people[j]['cm']:
                ranks[i] += 1

    return ranks

def main():
    n = int(input().strip())
    people = []

    for _ in range(n):
        kg, cm = map(int, input().split())
        people.append({'kg': kg, 'cm': cm})

    ranks = calculate_rank(people)
    print(' '.join(map(str, ranks)))

if __name__ == "__main__":
    main()
