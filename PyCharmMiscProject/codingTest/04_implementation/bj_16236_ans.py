from collections import deque
import heapq

def move(x, y):
    #상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque([(x,y)])
    graph = [[-1]*n for _ in range(n)]
    graph[x][y] = 0
    eat = []
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == -1:
                if spaces[nx][ny] <= shark:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
                    if 0 < spaces[nx][ny] < shark:
                        heapq.heappush(eat,(graph[nx][ny], nx, ny))
    return eat

n = int(input())
shark = 2
bx, by = 0, 0
spaces = []
result = 0
count = 0
for i in range(n):
    line = list(map(int,(input().split())))
    for j in range(n):
        if line[j] == 9:
            bx, by = i, j
    spaces.append(line)
spaces[bx][by] = 0

while True:
    eat = move(bx, by)
    if not eat:
        break
    else:
        distance, fx, fy = heapq.heappop(eat)
        result += distance
        spaces[fx][fy] = 0
        bx, by = fx, fy
        count += 1
        if count == shark:
            shark += 1
            count = 0

print(result)


