def find_parent(parent,x):
    if x != parent[x]:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,x,y):
    x = find_parent(parent,x)
    y = find_parent(parent,y)

    if x > y:
        parent[x] = y
    else:
        parent[y] =x

n = int(input())

data = []
for i in range(n):
    x,y,z = map(int,input().split())
    data.append((x,y,z,i))

parent = [i for i in range(n)]

costs = []
# x기준 정렬
data.sort(key = lambda x: x[0])
for i in range(n-1):
    cost = data[i+1][0] - data[i][0]
    costs.append((cost, data[i+1][3], data[i][3]))

# y기준 정렬
data.sort(key = lambda y: y[1])
for i in range(n-1):
    cost = data[i+1][1] - data[i][1]
    costs.append((cost, data[i+1][3], data[i][3]))

# z기준 정렬
data.sort(key = lambda z: z[2])
for i in range(n-1):
    cost = data[i+1][2] - data[i][2]
    costs.append((cost, data[i+1][3], data[i][3]))

costs.sort()
result = 0
for cost in costs:
    c, x, y = cost
    if find_parent(parent,x) != find_parent(parent,y):
        union_parent(parent,x,y)
        result += c

print(result)
