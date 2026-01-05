# m : 세로, n : 가로
m, n = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0

data = []
for _ in range(m):
    data.append(list(map(int, input().split())))

def dfs(x, y):
    global result
    now = data[x][y]
    if x == m-1 and y == n-1:
        result += 1
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if data[nx][ny] < now:
                    dfs(nx, ny)
        return

dfs(0,0)
print(result)











