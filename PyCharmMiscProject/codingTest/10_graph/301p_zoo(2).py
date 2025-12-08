def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

n, m = map(int, input().split())
parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i

edges= []
for i in range(m):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

result = 0
last = 0
edges.sort()
for edge in edges:
    c,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += c
        last = c

print(result - last)



