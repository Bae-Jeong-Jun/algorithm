from collections import deque
# m : 가로, n : 세로, h : 높이
m,n,h = map(int, input().split())
data = []
q = deque([])
dx = [0,0,-1,1,0,0]
dy = [-1,1,0,0,0,0]
dz = [0,0,0,0,-1,1]
result = 0

for floor in range(h):
    floors = []
    for line in range(n):
        lines = list(map(int, input().split()))
        for l in range(m):
            if lines[l] == 1:
                q.append((floor, line, l))
        floors.append(lines)
    data.append(floors)

while q:
    z, y, x = q.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
            if data[nz][ny][nx] == 0:
                data[nz][ny][nx] = data[z][y][x] + 1
                q.append((nz,ny,nx))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 0:
                print(-1)
                exit()
            result = max(result, data[i][j][k])

print(result-1)
