from collections import deque
def count(data):
    # 분리된 빙하 갯수
    ice = 0
    q = deque([])
    visited = [[False]*m for _ in range(n)]
    for a in range(1, n - 1):
        for b in range(1, m - 1):
            if data[a][b] > 0 and not visited[a][b]:
                ice += 1
                if ice >= 2:
                    return ice

                visited[a][b] = True
                q.append((a,b))
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                            if data[nx][ny] > 0:
                                visited[nx][ny] = True
                                q.append((nx,ny))

    return ice

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0
while True:
    count_ice = count(data)
    if count_ice == 0:
        print(0)
        break
    elif count_ice == 1:
        new_data = [[0]*m for _ in range(n)]
        for x in range(1, n - 1):
            for y in range(1, m - 1):
                if data[x][y] > 0:
                    melt = 0
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if data[nx][ny] == 0:
                                melt += 1
                    new_data[x][y] = max(new_data[x][y],data[x][y]-melt)

        data = new_data
        result += 1
    else:
        print(result)
        break








