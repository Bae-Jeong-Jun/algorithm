def find_shark():
    sharks = []
    for i in range(n):
        for j in range(n):
            if shark_field[i][j] != 0:
                sharks.append((shark_field[i][j], i, j))
                smell_field[i][j] = k #냄새뿌리기
    return sharks

def move_shark(sharks):
    # 상하좌우
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    for shark in sharks:
        shark_num, x, y = shark
        base_dir = shark_dir[shark_num][0]
        count = 0
        for next_dir in shark_dir[shark_num][base_dir]:
            if count == 4:
                nx, ny = x - dx[base_dir], y - dy[base_dir]
                shark_field[x][y] = 0
                shark_field[nx][ny] = shark_num
                for i in range(1,5):
                    if dx[i] == -dx[base_dir] and dy[i] == -dy[base_dir]:
                        shark_dir[shark_num][0] = i
            else:
                nx, ny = x + dx[next_dir], y + dy[next_dir]
                if 0 <= nx < n and 0 <= ny < n:
                    if smell_field[nx][ny] == 0:
                        shark_field[x][y] = 0
                        shark_field[nx][ny] = max(shark_num, shark_field[nx][ny])
                        shark_dir[shark_num][0] = next_dir
                    break
            count += 1

    # 냄새 지속 시간 줄이기
    for i in range(n):
        for j in range(n):
            if 0 < smell_field[i][j] <= k:
                smell_field[i][j] -= 1


# n X n
# m 마리 상어
# k초 간 냄새 유지
n, m, k = map(int, input().split())
answer = 0
smell_field = [[0]*n for _ in range(n)]

shark_field = []
for i in range(n):
    shark_field.append(list(map(int,input().split())))

# 상하좌우 = 1234
shark_dir=[[0] for _ in range(m+1)]
# 상어 처음 방향
dir_line = list(map(int,input().split()))
for i in range(1,m+1):
    shark_dir[i][0] = dir_line[i-1]
# 상어 방향 별 움직이는 우선순위
for i in range(1,m+1):
    for j in range(4):
        shark_dir[i].append(list(map(int, input().split())))

while True:
    sharks = find_shark()
    if len(sharks) == 1:
        break
    else:
        move_shark(sharks)
        answer += 1

print(answer)