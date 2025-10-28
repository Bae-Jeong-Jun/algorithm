# DFS : 모든 경로 탐색. 불필요한 경로도 탐색함
n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int,input())))

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1

result = 1e9
def dfs(i,j,count):
    global result
    if i == n-1 and j == m-1:
        result = min(result, count)
        return
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if visited[nx][ny] == 0 and data[nx][ny] == 1:
            visited[nx][ny] = 1
            dfs(nx,ny,count+1)
            visited[nx][ny] = 0

dfs(0,0,1)
print(result)