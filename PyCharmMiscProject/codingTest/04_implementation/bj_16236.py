import heapq

n = int(input())

space = []
fish = [[] for _ in range(7)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] not in (0,9):
            heapq.heappush(fish[line[j]], (i,j))
        if line[j] == 9:
            bx,by = i,j
    space.append(line)

shark = 2
distance = int(1e9)
nx, ny = 0, 0
for i in range(1,shark):
    for fish in fish[i]:
        fx, fy = fish
        if distance > abs(fx-bx) + abs(fy-by):
            distance = abs(fx-bx) + abs(fy-by)
            nx, ny = fx, fy
        elif distance == abs(fx-bx) + abs(fy-by):
            if fx < nx:
                nx, ny = fx, fy
            elif fx == nx:
                if fy < ny:
                    nx, ny = fx, fy

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph =[[0]*n for _ in range(n)]
for i in range(4):
    ddx = bx + dx[i]
    ddy = by + dy[i]
    if 0 <= ddx < n and 0 <= ddy < n:
        if space[ddx][ddy] <= space[bx][by]:
            graph[ddx][ddy] = graph[bx][by] + 1





