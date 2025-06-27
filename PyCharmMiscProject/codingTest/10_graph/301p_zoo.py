# N개의 집과 M개의 길
N, M = map(int, input().split())

# 부모 초기화
parent = [0] * (N+1)
for n in range(N+1):
    parent[n] = n

# 간선 정보
edges = [] * M

# A, B 간 유지비는 C
for _ in range(M):
    A, B, C = map(int,input().split())
    edges.append((C, A, B))
edges.sort() # 유지비 오름차순으로 정렬

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 합치기
def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x > y:
        parent[y]= x
    else:
        parent[x] = y

result = 0
last = 0 # 가장 비용 높은 간선
for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
        last = c

print(result - last) # 가장 높은 간선을 기준으로 마을 나눔