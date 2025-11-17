from collections import deque
def bfs(i,j,data):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k],y+dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if data[x][y] == data[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx,ny))

n = int(input())
data = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
normal = 0
# 동서남북
dx = [0,0,1,-1]
dy = [1,-1,0,0]

## normal
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j, data)
            normal += 1

## strange
s_data = [[i for i in row] for row in data]
for i in range(n):
    for j in range(n):
        if s_data[i][j] == "G":
            s_data[i][j] = "R"

visited = [[0]*n for _ in range(n)]
strange = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j, s_data)
            strange += 1

print(normal, strange)