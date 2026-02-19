import heapq
inf = int(1e9)

t = int(input())
for _ in range(t):
    n = int(input())
    data = []
    result = [[inf]*n for _ in range(n)]
    for _ in range(n):
        data.append(list(map(int,input().split())))
    result[0][0] = data[0][0]
    q = [(result[0][0], 0,0)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        dist,x,y = heapq.heappop(q)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                new_dist = dist + data[nx][ny]
                if result[nx][ny] > new_dist:
                    result[nx][ny] = new_dist
                    heapq.heappush(q,(new_dist,nx,ny))

    print(result[n-1][n-1])










