m, n = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

data = []
q = []
for i in range(m):
    line = list(map(int, input().split()))
    data.append(line)
    for j in range(n):
        q.append((line[j],i,j))

q.sort(reverse=True)
dp = [[0]*n for _ in range(m)]
dp[0][0] = 1
for sample in q:
    height, x, y = sample
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if data[nx][ny] < height:
                dp[nx][ny] += dp[x][y]

print(dp[m-1][n-1])
