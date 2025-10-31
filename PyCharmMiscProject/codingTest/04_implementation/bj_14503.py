# n*m 크기의 방
# 현재 위치 r,c
# 현재 방향 d 0 1 2 3
#           북동남서
n, m = map(int, input().split())
r, c, d = map(int, input().split())

data = []
visited =[[0]*m for _ in range(n)]
for i in range(n):
    data.append(list(map(int, input().split())))

# 북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def clean(x, y, d):
    if data[x][y] == 0 and visited[x][y] == 0:
        visited[x][y] = 1
    count = 0
    for i in range(1,5):
        nx, ny = x+dx[d-i], y+dy[d-i]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 1 or visited[nx][ny] == 1:
                count += 1
            else:
                visited[nx][ny] = 1
                d -= i
                if d < 0:
                    d += 4
                clean(nx,ny,d)
                return
    # 후진
    back = (d+2) % 4
    bx, by = x+dx[back], y+dy[back]
    if 0 <= bx < n and 0 <= by < m and data[bx][by] == 0:
        clean(bx, by, d)
    else:
        return

clean(r, c, d)
result = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            result += 1

print(result)