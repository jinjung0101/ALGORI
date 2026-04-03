def solution(park, routes):
    start_x, start_y = 0, 0
    start_x_temp, start_y_temp = 0, 0
    for i in range(len(park)):
        if 'S' in park[i]:
            start_x, start_y = i, park[i].index('S')

    for r in routes:
        temp = r.split()
        int_1 = int(temp[1])
        if temp[0] == 'E':
            start_y_temp += start_y
            for i in range(1, int_1):
                print(start_y + i)
                if start_y + i > len(park) or park[start_x][start_y + i] == 'X':
                    start_y = start_y_temp
                    break
                else:
                    start_y += i
        elif temp[0] == 'W':
            start_y_temp = start_y
            for i in range(1, int_1):
                print(start_y - i)
                if start_y - i > len(park) or park[[start_x][start_y - i]] == 'X':
                    break
                else:
                    start_y -= i    
        elif temp[0] == 'S':
            start_x_temp = start_x
            for i in range(1, int_1):
                print(start_x + i)
                if start_x + i > len(park[0]) or park[start_x + i][start_y] == 'X':
                    start_x = start_x_temp
                    break
                else:
                    start_x += i
        elif temp[0] == 'N':
            for i in range(1, int_1):
                start_x_temp = start_x
                print(start_x - i)
                if start_x - i > len(park[0]) or park[start_x - i][start_y] == 'X':
                    start_x = start_x_temp
                    break
                else:
                    start_x -= i

    return [start_x, start_y]


print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))