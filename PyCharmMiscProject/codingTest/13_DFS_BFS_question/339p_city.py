# n : 도시의 개수
# m : 단방향 도로의 개수
# k : 거리 정보
# x : 출발 도시 번호
n, m, k, x= map(int, input().split())

# 도시간 거리 초기화
data = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    data[a][b] = 1

result = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if data[x][i] == 0 and data[x][j] != 0 and data[j][i] != 0:
            data[x][i] = data[x][j] + data[j][i]

    if data[x][i] == k:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)