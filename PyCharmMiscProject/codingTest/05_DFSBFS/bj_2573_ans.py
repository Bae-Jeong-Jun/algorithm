from collections import deque

def count_ice():
    visited = [[False]*m for _ in range(n)]
    ice = 0

    for x, y in ice_list:
        if visited[x][y]:
            continue

        visited[x][y] = True
        ice += 1
        q = deque([(x,y)])
        while q:
            cx, cy = q.popleft()
            for k in range(4):
                nx, ny = cx + dx[k], cy + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and data[nx][ny] > 0:
                        visited[nx][ny] = True
                        q.append((nx,ny))

    return ice

n, m = map(int, input().split())
data = []
ice_list = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
year = 0

for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if data[i][j] > 0:
            ice_list.append((i,j))

while ice_list:
    if count_ice() >= 2:
        print(year)
        break

    new_ice_list = []
    melt_list = {}
    for ix, iy in ice_list:
        count = 0
        for k in range(4):
            nx, ny = ix+dx[k], iy+dy[k]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
                count += 1
        melt_list[(ix,iy)] = count

    for ix, iy in ice_list:
        new_height = data[ix][iy] - melt_list[(ix,iy)]
        if new_height > 0:
            new_ice_list.append((ix,iy))
            data[ix][iy] = new_height
        else:
            data[ix][iy] = 0

    ice_list = new_ice_list
    year += 1

else:
    print(0)




