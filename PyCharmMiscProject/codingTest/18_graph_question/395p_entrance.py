def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

g = int(input()) # 1 <= 탑승구의 수 <= 100000
p = int(input()) # 1 <= 비행기의 수 <= 100000

# 비어있으면 0. 아니면 비행기 번호 입력
parent = [0]*(g+1)
for i in range(g+1):
    parent[i] = i

count = 0
for _ in range(p):
    data = find_parent(parent, int(input()))
    if data == 0:
        break
    union_parent(parent, data, data-1)
    count += 1

print(count)





