# 시간 복잡도 n*m
from collections import deque

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

visited = [[0]*m for _ in range(n)]
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

count = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and data[i][j] == 0:
            queue= deque([(i, j)])
            visited[i][j] = 1
            count += 1

            while queue:
                a,b = queue.popleft()
                for k in range(4):
                    if 0 <= a+dx[k] < n and 0 <= b+dy[k] < m:
                        if data[a+dx[k]][b+dy[k]] == 0 and visited[a+dx[k]][b+dy[k]] == 0:
                            visited[a+dx[k]][b+dy[k]] = 1
                            queue.append((a+dx[k],b+dy[k]))

print(count)