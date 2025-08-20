def find_parents(parents,x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union_parents(parents, x, y):
    a = find_parents(parents, x)
    b = find_parents(parents, y)
    if a > b:
        parents[b] = a
    else:
        parents[a] = b

# 1 <= n(집의 수) <= 200000
# n -1 <= m(도로의 수) <= 200000
n, m = map(int, input().split())
edges = []
parents = [0]*n

for i in range(n):
    parents[i] = i

total = 0
for i in range(m):
    x, y, z = map(int, input().split())
    edges.append((z,x,y))
    total += z

edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parents(parents, a) != find_parents(parents, b):
        union_parents(parents, a, b)
        result += cost

print(total - result)

