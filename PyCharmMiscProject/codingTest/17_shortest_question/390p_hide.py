# n : 헛간 갯수
# m : 통로 갯수
n, m = map(int, input().split())

data = list([1e9]*(n+1) for _ in range(n+1))
for i in range(m):
    a,b = map(int, input().split())
    data[a][b] = 1
    data[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                data[i][j] = 0
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])
            data[j][i] = data[i][j]

for i in range(0, n+1):
    if data[1][i] == 1e9:
        data[1][i] = 0

num = 0
for i in range(1, n+1):
    if data[1][i] == max(data[1]):
        num = i
        break

count = 0
for i in range(1, n+1):
    if data[1][i] == max(data[1]):
        count += 1

print(num, max(data[1]), count)

