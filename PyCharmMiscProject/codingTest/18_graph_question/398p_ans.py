def find_parents(parents, x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union_parents(parents, x, y):
    x = find_parents(parents, x)
    y = find_parents(parents, y)

    if x > y:
        parents[y] = x
    else:
        parents[x] = y

n = int(input())

x = []
y = []
z = []
for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

edges = [] # 간선 정보 저장
for i in range(n-1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))
edges.sort()

parents = [0]*(n+1)
for i in range(1, n+1):
    parents[i] = i

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parents(parents, a) != find_parents(parents, b):
        union_parents(parents, a, b)
        result += cost

print(result)



