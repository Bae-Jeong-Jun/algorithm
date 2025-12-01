def find_parents(parents,x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union_parents(x, y, parents):
    x = find_parents(parents, x)
    y = find_parents(parents, y)
    if x >= y:
        parents[x] = y
    else:
        parents[y] = x

# v : 노드의 갯수, e : 간선의 갯수
v, e = map(int, input().split())
parents = [0]*(v+1)

for i in range(1, v+1):
    parents[i] = i

for _ in range(e):
    a, b = map(int, input().split())
    # if find_parents(parents, a) == find_parents(parents, b):
    #     print("싸이클 발생")
    union_parents(a, b, parents)

# 각 원소가 속한 집합
for i in range(1, v+1):
    print(find_parents(parents, i))

# 부모 테이블
for i in range(1, v+1):
    print(parents[i])







