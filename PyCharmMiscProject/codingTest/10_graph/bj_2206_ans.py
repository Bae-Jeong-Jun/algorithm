from collections import deque
import sys

n, m = map(int,input().split())
data = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 0은 벽 안부슴, 1은 이미 부슴
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for _ in range(n):
    data.append(list(map(int, input())))

q = deque([(0,0,0)])
while q:
    x, y, broken = q.popleft()
    if x == n-1 and y == m-1:
        print(visited[x][y][broken])
        sys.exit()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                visited[nx][ny][broken] = visited[x][y][broken] + 1
                q.append((nx,ny,broken))
            elif data[nx][ny] == 1 and broken == 0 and visited[nx][ny][1] == 0:
                visited[nx][ny][1] = visited[x][y][broken] + 1
                q.append((nx,ny,1))

print(-1)










