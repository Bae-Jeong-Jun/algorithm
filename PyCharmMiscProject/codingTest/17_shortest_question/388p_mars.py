import heapq
t = int(input())
for _ in range(t):
    data = []
    n = int(input())
    for _ in range(n):
        data.append(list(map(int, input().split())))

    check_data = [[1e9]*n for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = [(data[0][0], 0, 0)]
    check_data[0][0] = data[0][0]

    while q:
        # 거리 짧은 순 부터 pop
        dist, x, y = heapq.heappop(q)
        if x == n-1 and y == n-1:
            print(check_data)
            print(dist)

        if dist > check_data[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                new_dist = dist + data[nx][ny]
                if new_dist < check_data[nx][ny]:
                    check_data[nx][ny] = new_dist
                    heapq.heappush(q, (new_dist, nx, ny))