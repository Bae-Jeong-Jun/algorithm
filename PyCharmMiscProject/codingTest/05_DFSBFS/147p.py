# 너비 우선 탐색
# O(N) DFS 보다 실제 수행시간 면에서 유리함
from collections import deque
def bfs(graph, i, visited):
    queue = deque([i])
    visited[i] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for j in graph[v]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True

graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]
         ]
visited = [False]*9

bfs(graph, 1, visited)