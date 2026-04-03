# # 그래프 동서남북 모두 탐색하며 1로 이어져있는곳 (만약 동서남북 모두 1이라면?)
# # 그림 list index에 += 1 하면서 저장 끝나면 다음..다음..
# # 방문한곳저장
# # 그림 list의 len과 제일 큰 값 출력 

# import sys
# from collections import deque

# n, m = map(int, sys.stdin.readline().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, sys.stdin.readline().split())))

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# def bfs(graph, a, b):
#     queue = deque()
#     queue.append((a, b))
#     graph[a][b] = 0
#     count = 1

#     while
