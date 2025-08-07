# 1 <= n,m <= 500
# 여행지 n개
# 여행 계획에 속한 여행지 m개
def find_parent(parent, z):
    if z != parent[z]:
        parent[z] = find_parent(parent, parent[z])
    return parent[z]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        # 여행지간 길이 있을 때
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

plan = list(map(int, input().split()))
plan = plan[:m]

result = True

for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

if result:
    print("YES")
else:
    print("NO")













