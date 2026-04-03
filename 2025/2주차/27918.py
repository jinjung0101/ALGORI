play_num = int(input())
dal = 0
ponix = 0
for i in range(play_num):
    winner = str(input())
    if dal - ponix == 2 or dal - ponix == -2:
        continue
    else:
        if winner == "D":
            dal += 1
        elif winner == "P":
            ponix += 1

print(f'{dal}:{ponix}')