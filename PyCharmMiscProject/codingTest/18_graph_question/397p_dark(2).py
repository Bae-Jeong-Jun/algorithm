def find_parents(parents, x):
    if x != parents[x]:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union_parents(parents, x, y):
    x = find_parents(parents, x)
    y = find_parents(parents, y)

    if x > y:
        parents[x] = y
    else:
        parents[y] = x

n, m = map(int, input().split())
parents = [0]*n
for i in range(n):
    parents[i] = i

data = []
for _ in range(m):
    x,y,z = map(int, input().split())
    data.append((z,x,y))

data.sort()
result = 0
for sample in data:
    cost, x, y = sample
    if find_parents(parents,x) == find_parents(parents,y):
        result += cost
    else:
        union_parents(parents,x,y)

print(result)






