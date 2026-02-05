from collections import deque
import copy
import sys
inf = int(1e9)
input = sys.stdin.readline

n, m = map(int,(input().split()))
data = []
q_1 = deque([])
da = [-1,1,0,0]
db = [0,0,-1,1]
result = inf

def dfs(a,b,new_data,visited):
    global result
    if a == n-1 and b == m-1:
        result = min(result, new_data[n-1][m-1])
        return
    for i in range(4):
        na, nb = a + da[i], b + db[i]
        if 0 <= na < n and 0 <= nb < m and new_data[na][nb] != -1:
            if not visited[na][nb]:
                new_data[na][nb] = new_data[a][b] + 1
                visited[na][nb] = True
                dfs(na, nb, new_data, visited)
                new_data[na][nb] = 0
                visited[na][nb] = False
    return

for i in range(n):
    line = list(map(int,input()))
    for j in range(m):
        if line[j] == 1:
            q_1.append((i,j))
            line[j] = -1 #벽을 -1로 두기
    data.append(line)

while q_1:
    x,y = q_1.popleft()
    new_data = copy.deepcopy(data)
    new_data[0][0] = 1
    new_data[x][y] = 0
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    dfs(0,0,new_data,visited)

print(result)







