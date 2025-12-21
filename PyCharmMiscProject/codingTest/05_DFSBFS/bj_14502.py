from collections import deque
import itertools
import copy

def start(v_data, virus):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if v_data[nx][ny] == 0:
                    v_data[nx][ny] = 2
                    q.append((nx, ny))

    total = 0
    for i in range(n):
        for j in range(m):
            if v_data[i][j] == 0:
                total += 1
    return total

n, m = map(int, input().split())
answer = 0
data = []
space = []
virus = []
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 0:
            space.append((i,j))
        if line[j] == 2:
            virus.append((i,j))
    data.append(line)

for comb in itertools.combinations(space,3):
    v_data = copy.deepcopy(data)
    for i in range(3):
        x, y = comb[i]
        v_data[x][y] = 1
    answer = max(answer, start(v_data, virus))

print(answer)