# 신장그래프(Spanning Tree) : 하나의 그래프가 있을 때 모든 노드를 포함하면서
# 사이클이 존재하지 않는 부분 그래프

# 크루스칼 알고리즘(Kruskal Algorithm)
# 최소 신장 트리 알고리즘 : 최소 비용으로 만들 수 있는 신장 트리
# 가장 거리가 짧은 간선부터 차례대로 집합에 추가(사이클 발생하는 간선 제외)
# 시간 복잡도 : O(ElogE)

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

# 노드와 간선 각각의 갯수
V, E = map(int, input().split())

# 간선 정보 저장
Edge = []
for e in range(E):
    a, b, cost = map(int, input().split())
    Edge.append((cost, a, b))

# 부모 초기화
parent = [0] * (V+1)
for v in range(1, V+1):
    parent[v] = v

result = 0
Edge.sort()
for edge in Edge:
    cost, a, b = edge
    # 사이클 발생하지 않을 때만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


