days, socks = map(int, input().split())
price = list(map(int, input().split()))
lowest_price = price[0]*socks + price[1]*socks
for i in range(days-1):
    new_price = price[i]*socks + price[i+1]*socks
    if new_price < lowest_price:
        lowest_price = new_price

print(lowest_price)