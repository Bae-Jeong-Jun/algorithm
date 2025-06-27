# 무방향 그래프에서 사이클 판별 가능

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 노드, 간선
V, E = map(int, input().split())

# 부모 노드 자기 자신으로 초기화
parent = [0] * (V+1)
for v in range(1, V+1):
    parent[v] = v

cycle = False

# 간선 입력
for e in range(E):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
    else:
        union_parent(parent, a, b)

if cycle:
    print('Cycle 발생')
else:
    print('Cycle 발생하지 않음')















