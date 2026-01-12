import heapq

def find_parent(parent,x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,x,y):
    x = find_parent(parent,x)
    y = find_parent(parent,y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

parent = [i for i in range(n)]
costs = []
for i in range(n-1):
    xi, yi, zi = data[i]
    for j in range(i+1, n):
        xj, yj, zj = data[j]
        cost = min(abs(xi-xj), abs(yi-yj), abs(zi-zj))
        heapq.heappush(costs,(cost,i,j))

result = 0
while costs:
    c, x, y = heapq.heappop(costs)
    if find_parent(parent,x) != find_parent(parent,y):
        union_parent(parent,x,y)
        result += c

print(result)