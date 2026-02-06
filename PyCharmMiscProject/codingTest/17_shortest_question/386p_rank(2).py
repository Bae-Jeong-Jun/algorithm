n, m = map(int,input().split())
data = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int,input().split())
    # a < b
    data[a-1][b-1] = 1
    data[b-1][a-1] = -1

for k in range(n):
    for i in range(n):
        if data[i][k] == 0:
            continue
        for j in range(n):
            if data[k][j] == 0:
                continue
            if data[i][k] == data[k][j]:
                data[i][j] = data[i][k]
                data[j][i] = -data[i][k]

result = 0
for i in range(n):
    check = True
    for j in range(n):
        if i != j:
            if data[i][j] == 0:
                check = False
                break
    if check:
        result += 1
print(result)
