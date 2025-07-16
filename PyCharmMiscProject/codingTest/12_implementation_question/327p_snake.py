n = int(input()) # 보드의 크기
k = int(input()) # 사과 개수

array = [[0]*(n+1) for _ in range(n+1)] # 맵 정보

# 사과 위치 저장
for _ in range(k):
    a, b = map(int, input().split())
    array[a][b] = 1

# 뱀의 방향 전환 횟수
l = int(input())
change = []

# x 초 후에 c==L 이면 왼쪽, c==D 이면 오른쪽으로 회전
for _ in range(l):
    x, c = input().split()
    change.append((int(x), c))

#    동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    array[x][y] = 2
    q = [(x, y)]
    direction = 0
    time = 0
    index = 0

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx <= n and 1 <= ny <= n and array[nx][ny] != 2:
            # 사과 없으면 꼬리 제거
            if array[nx][ny] == 0:
                array[nx][ny] = 2
                q.append((nx, ny))
                ox, oy = q.pop(0)
                array[ox][oy] = 0
            # 사과 있으면 꼬리 그대로 두기
            if array[nx][ny] == 1:
                array[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1

        # 정해진 시간에 방향 회전
        if index < l and time == change[index][0]:
            direction = turn(direction, change[index][1])
            index += 1
    return time

print(simulate())


