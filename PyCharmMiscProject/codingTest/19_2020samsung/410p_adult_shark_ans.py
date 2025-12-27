# n X n
# m 마리 상어
# k초 간 냄새 유지
n,m,k = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
direction = [0]+list(map(int, input().split()))

priority = [[] for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(4):
        priority[i].append(list(map(int, input().split())))

# 몇번 상어 냄새가 몇초간 지속되는지
smell = [[[0,0] for _ in range(n)] for _ in range(n)]

def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if array[i][j] > 0:
                smell[i][j][0] = array[i][j]
                smell[i][j][1] = k

def move():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    new_array = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            found = False
            if array[x][y] > 0:
                num = array[x][y]
                dir = direction[num] - 1
                for index in priority[num][dir]:
                    nx = x + dx[index-1]
                    ny = y + dy[index-1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0:
                            direction[num] = index
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = num
                            else:
                                new_array[nx][ny] = min(new_array[nx][ny],num)
                            found = True
                            break

                if found:
                    continue
                else:
                    for index in priority[num][dir]:
                        nx = x + dx[index - 1]
                        ny = y + dy[index - 1]
                        if 0 <= nx < n and 0 <= ny < n:
                            if smell[nx][ny][0] == num:
                                direction[num] = index
                                if new_array[nx][ny] == 0:
                                    new_array[nx][ny] = num
                                else:
                                    new_array[nx][ny] = min(new_array[nx][ny], num)
                                break

    return new_array

time = 0
while True:
    update_smell()
    array = move()
    time += 1

    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False
    if check:
        print(time)
        break

    if time >= 1000:
        print(-1)
        break










