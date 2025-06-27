# 노드, 간선 수가 많을 땐 다익스트라 알고리즘(우선순위 큐 이용)
# 노드 개수가 적으면 플로이드 워셜 알고리즘 이용

# 서로소 집합 알고리즘
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

# 노드와 간선
V, E = map(int, input().split())

# 부모 노드 자기 자신으로 초기화
parent = [0] * (V+1)
for v in range(1, V+1):
    parent[v] = v

# 간선 정보
for e in range(E):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합 : ', end='')
for v in range(1, V+1):
    print(find_parent(parent, v), end=' ')

print('부모 테이블 : ', end='')
for v in range(1, V+1):
    print(parent[v], end=' ')














