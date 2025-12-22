import copy
from collections import deque
n, m = map(int, input().split())
data = []
virus = []
answer = 0

def start(data, virus):
    total = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque(virus)
    v_data = copy.deepcopy(data)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if v_data[nx][ny] == 0:
                    v_data[nx][ny] = 2
                    q.append((nx,ny))

    for j in range(n):
        for k in range(m):
            if v_data[j][k] == 0:
                total += 1
    return total

def dfs(count):
    global answer
    if count == 3:
        answer = max(answer, start(data, virus))
        return
    else:
        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    data[i][j] = 1
                    dfs(count+1)
                    data[i][j] = 0

for i in range(n):
    line = list(map(int, input().split()))
    data.append(line)
    for j in range(m):
        if line[j] == 2:
            virus.append((i,j))

dfs(0)
print(answer)

