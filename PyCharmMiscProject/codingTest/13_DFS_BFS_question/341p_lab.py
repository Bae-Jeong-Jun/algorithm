# 깊이 우선 탐색

# 지도 크기 세로 크기 n X 가로 크기 m
# 3 <= n, m <= 8
n, m = map(int, input().split())

# 0 : 빈칸, 1 : 벽, 2 : 바이러스
# 3 <= 빈칸
# 2 <= 바이러스 <= 10
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

temp = [[0]*m for _ in range(n)]
result = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)













