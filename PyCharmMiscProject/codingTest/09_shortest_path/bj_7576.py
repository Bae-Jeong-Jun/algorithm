from collections import deque
# m : 가로 칸 | n : 세로 칸
# 1 : 익은 토마토 | 0 : 안 익은 토마토
m, n = map(int, input().split())
box = []
for i in range(n):
    box.append(list(map(int, input().split())))

#북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))

def start():
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == 0:
                    box[nx][ny] = box[x][y] + 1
                    q.append((nx,ny))

start()

result = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        result = max(result, box[i][j])

print(result-1)


