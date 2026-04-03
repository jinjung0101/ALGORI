#서울 터미널의 교통편의 개수 N, D는 i번째 교통편의 도착지, C는 i번째 교통편의 요금
N = int(input())
expensive_city = []
expensive_city_num = 0
jinju_city = 0
for i in range(N):
    D, C = map(str, input().split())
    if D == "jinju":
        jinju_city += int(C)
    else:
        expensive_city.append(int(C))
print(jinju_city)
for i in expensive_city:
    if i > jinju_city:
        expensive_city_num += 1
print(expensive_city_num)
