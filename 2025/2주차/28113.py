# N: 역까지 도보 시간 A: 버스, B: 지하철, 
# 1. 버스 시간이 지하철 시간보다 더 짧다 -> 버스를 탄다
# 2. 버스 시간이 지하철 시간보다 더 길다 -> 지하철을 탄다
# 2 - 1. 도보시간이 지하철시간보다 길다 -> 버스를 탄다. 
# 버스 시간과 지하철 시간이 같으면 -> "Anything"
# 지하철 시간이 더 짧지만 보도 시간 버스 시간보다 길면 -> Bus
N, A, B = map(int, input().split())
if A < B:
    print("Bus")
elif A > B:
    if N > B:
        print("Bus")
    else:
        print("Subway")
else:
    print("Anything")