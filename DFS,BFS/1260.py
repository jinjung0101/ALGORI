from collections import deque


def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node] - set(visited))
    
    return visited

graph = [[1, 2],
[1, 3],
[1, 4],
[2, 4],
[3, 4]]

bfs(graph, 1)