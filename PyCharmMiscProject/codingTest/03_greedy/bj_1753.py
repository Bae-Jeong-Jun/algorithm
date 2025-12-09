import sys
import heapq
input = sys.stdin.readline
def dijkstra(x):
    distance[x] = 0
    q = []
    heapq.heappush(q,(0,x))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        else:
            for nxt, w in graph[now]:
                cost = dist + w
                if distance[nxt] > cost:
                    distance[nxt] = cost
                    heapq.heappush(q,(cost,nxt))

v, e = map(int, input().split())
k = int(input()) # 시작 정점
graph = [[]for _ in range(v+1)]
INF = int(1e9)
distance = [INF] * (v+1)

for i in range(e):
    u,y,w = map(int, input().split())
    graph[u].append((y,w))

dijkstra(k)

for i in range(1, v+1):
    if distance[i] != INF:
        print(distance[i])
    else:
        print("INF")
