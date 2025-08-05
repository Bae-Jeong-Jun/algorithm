n = int(input()) # 1 <= 도시 갯수 <= 100
m = int(input()) # 1 <= 버스 갯수 <= 100000

inf = int(1e9)
data = [[inf]*(n+1) for _ in range(n+1)]
for _ in range(m):
    # 시작, 도착, 비용
    a,b,c = map(int, input().split())
    if data[a][b] != inf:
        data[a][b] = min(data[a][b], c)
    else:
        data[a][b] = c

for k in range(1, n + 1):
    for i in range(1, n+1):
        for j in range(1, n + 1):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if data[i][j] != inf:
            print(data[i][j], end=' ')
        else:
            print(0, end=' ')
    print()
