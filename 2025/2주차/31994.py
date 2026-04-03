the_king_semina = ""
king_num = 0
for i in range(7):
    semina, num = input().split()
    if int(num) > king_num:
        king_num = int(num)
        the_king_semina = semina
    else:
        continue

print(the_king_semina)
