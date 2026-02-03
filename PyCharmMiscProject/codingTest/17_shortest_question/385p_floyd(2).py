inf = int(1e9)
n = int(input())
m = int(input())
data = [[inf]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    data[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    data[a][b] = min(data[a][b],c)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if data[i][j] == inf:
            print(0, end=" ")
        else:
            print(data[i][j], end=" ")
    print()