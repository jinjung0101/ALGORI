def solution(n):
    answer = [[0 for j in range(n)] for i in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y, current = 0, 0, 1
    answer[0][0] = 1
    while True:
        if current == n * n:
            break

        # right dx[0], dy[0]
        while True:
            nx, ny = x + dx[0], y + dy[0]
            if n <= ny or answer[nx][ny] != 0:
                break
            if 0 <= ny < n:
                if answer[nx][ny] == 0:
                    x, y = nx, ny
                    current += 1
                    answer[x][y] = current 
                    print(answer)
                
        # bottom
        while True:
            nx, ny = x + dx[1], y + dy[1]
            if n <= nx or answer[nx][ny] != 0:
                break
            if 0 <= nx < n:
                if answer[nx][ny] == 0:
                    x, y = nx, ny
                    current += 1
                    answer[x][y] = current 
                    print(answer)

        # left
        while True:
            nx, ny = x + dx[2], y + dy[2]
            if ny < 0 or answer[nx][ny] != 0:
                break
            if 0 <= ny < n:
                if answer[nx][ny] == 0:
                    x, y = nx, ny
                    current += 1
                    answer[x][y] = current
                    print(answer)

        # top
        while True:
            nx, ny = x + dx[3], y + dy[3]
            if nx < 0 or answer[nx][ny] != 0:
                break
            if 0 <= nx < n:
                if answer[nx][ny] == 0:    
                    x, y = nx, ny
                    current += 1
                    answer[x][y] = current
                    print(answer)

    return answer

print(solution(4))