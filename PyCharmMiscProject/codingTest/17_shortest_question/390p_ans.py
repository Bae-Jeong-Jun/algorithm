import heapq
# n : 헛간 갯수
# m : 통로 갯수
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    # a <-> b 거리 1
    graph[a].append((b,1))
    graph[b].append((a,1))

INF = int(1e9)
distance = [INF]*(n+1)
distance[1] = 0

# 거리, 노드
q=[]
heapq.heappush(q, (0, 1))
while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
        continue
    for nxt, cost in graph[node]:
        new_dist = dist + cost
        if new_dist < distance[nxt]:
            distance[nxt] = new_dist
            heapq.heappush(q, (new_dist, nxt))

max_dist = max([d for d in distance[1:] if d != INF])
index = distance.index(max_dist)
count = distance.count(max_dist)

print(index,max_dist,count)






