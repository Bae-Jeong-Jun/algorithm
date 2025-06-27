# 위상 정렬 : 순서가 정해져 있는 일련의 작업을
# 차례대로 수행해야 할 때 사용할 수 있는 알고리즘
# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열
# 진입 차수 : 들어오는 간선 개수
# 시간 복잡도 : O(V+E)

from collections import deque

# 노드와 간선
V, E = map(int,input().split())

# 진입 차수 초기화
indegree = [0] * (V+1)

# 간선 정보
graph = [[]for v in range(V+1)]
for _ in range(E):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1 #진입 차수 증가

q = deque()
result = []

def topology_sort():
    for v in range(1, V+1):
        if indegree[v] == 0:
            q.append(v)

    while q:
        x = q.popleft()
        result.append(x)
        for g in graph[x]:
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)

    print(result)

topology_sort()






