from collections import deque
n, m = map(int,(input().split()))

data = []
for _ in range(n):
    data.append(list(map(int,(input()))))

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque([(0,0)])
while queue:
    x,y = queue.popleft()
    if x == n-1 and y == m-1:
        print(data[x][y])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 1:
                data[nx][ny] = data[x][y] + 1
                queue.append((nx,ny))













