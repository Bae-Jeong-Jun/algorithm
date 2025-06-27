# 특정지점에서 지점까지 최단거리는 다익스트라
# 모든지점에서 모든지점까지 최단거리는 플로이드 워셜 알고리즘

INF = int(1e9)
import heapq

# N : 도시의 개수 / M : 통로의 개수 /C : C도시 번호
N, M, C = map(int, input().split())

distance = [INF] * (N+1)

graph = [[] for n in range(N+1)]

# X -> Y 까지 Z시간 걸림
for m in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y,Z))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0,start))
    while q: #q가 있을 때
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for g in graph[now]:
            cost = dist + g[1]
            if distance[g[0]] > cost:
                distance[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))

dijkstra(C)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count-1, max_distance)











