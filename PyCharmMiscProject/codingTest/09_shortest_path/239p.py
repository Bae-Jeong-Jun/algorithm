# E : 간선의 갯수, V : 노드의 갯수
# 시간 복잡도 : O(ElogV)
# heap 자료구조 이용 : 하나의 데이터 삽입, 삭제시 O(logN)

import heapq
INF = int(1e9)

def dijkstra(start):
    q = [] # 거리와 노드
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 처리된 거는 무시
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# 노드, 간선
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
distance[start] = 0

#[a]= (b,c) : a에서 b까지 거리는 c
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('infinity')
    else:
        print(distance[i])


