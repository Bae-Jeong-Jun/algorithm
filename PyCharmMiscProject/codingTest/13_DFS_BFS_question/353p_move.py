from collections import deque

def find(i,j):
    visited[i][j] = True
    q = deque()
    q.append((i,j))
    move = []
    move.append((i,j))
    total = data[i][j]
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(data[nx][ny] - data[x][y]) <= r:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    move.append((nx,ny))
                    total += data[nx][ny]
    return move, total

n,l,r = map(int, input().split())
# n*n 크기 땅
# l <= 인구 차이 <= r 일 때 국경 open(연합)
# 연합 각칸의 인구수 = 연합 인구수 // 연합 칸의 개수

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
dx = [0,1,0,-1]
dy = [1,0,-1,0]

answer = 0
while True:
    moved = False
    # 하루마다 방문 초기화
    visited = list([False]*n for _ in range(n))

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                move, total = find(i,j)
                if len(move) > 1:
                    moved = True
                    new_pop = total // len(move)
                    for x,y in move:
                        data[x][y] = new_pop

    if not moved:
        break
    answer += 1

print(answer)