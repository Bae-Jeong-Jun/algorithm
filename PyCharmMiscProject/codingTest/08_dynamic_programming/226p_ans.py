n, m = map(int,input().split())
coins = [int(input()) for _ in range(n)]

INF = 1e9
d = [INF]*10001
d[0] = 0

for coin in coins:
    for i in range(coin, m+1):
        if d[i-coin] != INF:
            d[i] = min(d[i], d[i-coin] + 1)

if d[m] == INF:
    print(-1)
else:
    print(d[m])