n, m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
max_val = max(map(max,data))
visited = [[False]*m for _ in range(n)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,total,count):
    global answer
    count += 1

    if total + max_val*(4-count) <= answer:
        return

    if count == 4:
        answer = max(answer, total)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, total + data[nx][ny], count)
            visited[nx][ny] = False

def check_t(x,y):
    global answer
    for i in range(4):
        total_t = data[x][y]
        for j in range(3):
            k = (i+j)%4
            nx = x + dx[k]
            ny = y + dy[k]
            if not (0<=nx<n and 0<=ny<m):
                break
            total_t += data[nx][ny]
        else: #break 없이 3칸 성공시
            answer = max(answer, total_t)

answer = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,data[i][j],0)
        visited[i][j] = False
        check_t(i,j)

print(answer)





