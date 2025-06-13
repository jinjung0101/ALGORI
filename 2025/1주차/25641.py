st_num = int(input())
ST = list(input()) 

for i in range(st_num-1):
    if ST.count('s') ==  ST.count('t'):
        print(''.join(ST))
        break
    else:
        ST.pop(0)

