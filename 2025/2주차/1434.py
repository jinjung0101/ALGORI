# 박스의 개수 N, 책의 개수 M
N, M = map(int, input().split())
box_book = []
# books_num = M
box_book.append(list(map(int, input().split())))
box_book.append(list(map(int, input().split())))

used = [False] * M
# while books_num != 0:
#     for box in range(N):
#         for book in range(M):
#             if box_book[0][box] < box_book[1][book]:
#                 continue
#             else:
#                 box_book[0][box] -= box_book[1][book]
#                 books_num -= 1
for box in range(N):
    for book in range(M):
        if used[book]:
            continue
        if box_book[0][box] >= box_book[1][book]:
            box_book[0][box] -= box_book[1][book]
            used[book] = True
answer = 0

for i in range(N):
    answer += box_book[0][i]

print(answer)
