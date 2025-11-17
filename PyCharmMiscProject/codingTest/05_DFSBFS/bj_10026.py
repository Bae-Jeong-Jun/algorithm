def dfs(i, j):
    visited[i][j] = 1
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            if data[nx][ny] == data[i][j]:
                dfs(nx, ny)

def s_dfs(i, j):
    s_visited[i][j] = 1
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < n and 0 <= ny < n and s_visited[nx][ny] == 0:
            if s_data[nx][ny] == s_data[i][j]:
                s_dfs(nx, ny)

n = int(input())
data = [list(input()) for _ in range(n)]
s_data = [["R"]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if data[i][j] == "G":
            s_data[i][j] = "R"
        else:
            s_data[i][j] = data[i][j]

visited = [[0]*n for _ in range(n)]
s_visited = [[0]*n for _ in range(n)]
normal = 0
strange = 0 #R, G를 같은색으로 봄

# 동서남북
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            normal += 1

for i in range(n):
    for j in range(n):
        if s_visited[i][j] == 0:
            s_dfs(i,j)
            strange += 1

print(normal, strange)







