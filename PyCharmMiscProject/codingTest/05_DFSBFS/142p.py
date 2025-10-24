# 깊이 우선 탐색 (재귀함수 이용)
# O(N)
def dfs(graph, i, visited):
    visited[i] = True
    print(i, end=' ')
    for j in graph[i]:
        if visited[j] == False:
            dfs(graph, j, visited)

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

dfs(graph, 1, visited)