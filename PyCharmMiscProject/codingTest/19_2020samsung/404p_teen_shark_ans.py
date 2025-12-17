import copy
data = []
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
answer = 0

def find_fish(data,x):
    for i in range(4):
        for j in range(4):
            if data[i][j][0] == x:
                return i,j
    return None

def move_fish(data,sx,sy):
    for i in range(1,17):
        pos = find_fish(data,i)
        if not pos:
            continue

        fx, fy = pos
        f_num, f_dir = data[fx][fy]
        for j in range(8):
            nd = (f_dir + j)%8
            nx = fx + dx[nd]
            ny = fy + dy[nd]
            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == sx and ny == sy):
                data[fx][fy] = data[nx][ny]
                data[nx][ny] = (f_num, nd)
                break

def dfs(sx,sy,total,data):
    global answer
    answer = max(answer, total)
    data = copy.deepcopy(data)

    # 현재 위치 물고기 먹기
    num, dir = data[sx][sy]
    data[sx][sy] = (-1,-1)

    # 물고기 이동
    move_fish(data,sx,sy)

    # 상어 이동
    for step in range(1,4):
        nx = sx + dx[dir]*step
        ny = sy + dy[dir]*step

        if 0<= nx < 4 and 0<= ny < 4:
            if data[nx][ny][0] > 0:
                dfs(nx,ny,total+data[nx][ny][0],data)

for _ in range(4):
    line = list(map(int, input().split()))
    row = []
    for j in range(0,8,2):
        row.append((line[j],line[j+1]-1))
    data.append(row)

dfs(0,0,data[0][0][0],data)
print(answer)