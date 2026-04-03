from collections import deque
import sys

# def bfs(grapfh, node, visited):
#     queue = deque([node])
#     visited[node] = True

#     while queue:
#         current = queue.popleft()
#         print(current, end=' ')

#         for neighbor in grapfh[current]:
#             if not visited[neighbor]:
#                 visited[neighbor] = True
#                 queue.append(neighbor)  

# A, B = map(int, input().split())

# painting = []
# for i in range(A):
#     painting.append(list(map(int, input().split())))

# visited = [[False] * B for _ in range(A)]
A, B = map(int, sys.stdin.readline().split() )
visited = [[False] * B for _ in range(A)]
components_size = []

def bfs(start_x, start_y):
    q = deque([(start_x, start_y)])
    return q


def count_components(board):
    return()
