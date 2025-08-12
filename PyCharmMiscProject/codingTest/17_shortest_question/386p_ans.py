# 학생 수 : 2 <= n <= 500
# 성적 비교 횟수 : 2 <= m <=10000
n, m = map(int, input().split())

data = list([0]*(n+1) for _ in range(n+1))

# 성적 : a < b
for _ in range(m):
    a, b = map(int, input().split())
    data[a][b] = 1

for k in range(n+1):
    for i in range(n + 1):
        for j in range(n + 1):
            if data[i][k] and data[k][j]:
                data[i][j] = 1

result = 0
for i in range(1, n+1):
    lower = sum(data[j][i] for j in range(1, n+1))
    higher = sum(data[i][j] for j in range(1, n+1))
    if lower + higher == n-1:
        result += 1
print(result)