from collections import deque

n, k = map(int, input().split())

graph = [] # 시험관
data = [] # 바이러스 정보
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
                        #바이러스, 시간, 위치 정보
            data.append((graph[i][j], 0, i, j))

data.sort() #바이러스 번호 오름차순으로 정렬
q = deque(data)

# s초 뒤의 x, y의 바이러스 종류
s, x, y = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
while q:
    virus, time, a, b = q.popleft()
    if time == s:
        break
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, time+1, nx, ny))

print(graph)
print(graph[x-1][y-1])


