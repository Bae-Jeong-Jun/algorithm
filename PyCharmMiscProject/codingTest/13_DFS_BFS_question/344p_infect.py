# n X n : 시험관 크기 1 <= n <= 200
# k : 바이러스 종류 수 1 <= k <= 1000
n, k = map(int, input().split())

# 시험관 배치
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# s초 뒤에 (x,y)의 바이러스 종류
s, x, y = map(int, input().split())

time = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def infect(a, b):
    global time, nx, ny
    while time != s:
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] == 0:
                    data[nx][ny] = data[a][b]
        time += 1
        infect(nx, ny)

count = 1
while count <= k:
    for i in range(n):
        for j in range(n):
            if count == data[i][j]:
                infect(i, j)
    count += 1

print(data)
print(data[x-1][y-1])


















