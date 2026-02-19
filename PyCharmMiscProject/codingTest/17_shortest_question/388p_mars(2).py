def dfs(x,y,data_sum):
    global result
    if x == n-1 and y == n-1:
        result = min(result, data_sum)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx, ny = x + dx[i] , y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            data_sum += data[nx][ny]
            visited[nx][ny] = True
            dfs(nx,ny,data_sum)
            data_sum -= data[nx][ny]
            visited[nx][ny] = False

    return result

t = int(input())
for _ in range(t):
    n = int(input())
    result = int(1e9)
    data = []
    visited = [[False]*n for _ in range(n)]
    for _ in range(n):
        data.append(list(map(int,input().split())))
    visited[0][0] = True
    print(dfs(0,0, data[0][0]))