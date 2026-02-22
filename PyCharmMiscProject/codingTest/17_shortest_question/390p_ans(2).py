import heapq
inf = int(1e9)
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    # 거리, 노드
    graph[a].append((1,b))
    graph[b].append((1,a))

distance = [inf]*(n+1)
distance[1] = 0

q = []
heapq.heappush(q, (0,1))
while q:
    dist, node = heapq.heappop(q)
    if dist > distance[node]:
        continue
    for i in graph[node]:
        nxt_dist, nxt = i
        if distance[nxt] > dist + nxt_dist:
            distance[nxt] = dist + nxt_dist
            heapq.heappush(q, (distance[nxt], nxt))

max_dist = max([d for d in distance[1:] if d != inf])
index = distance.index(max_dist)
count = distance.count(max_dist)

print(index,max_dist,count)
print(distance)




