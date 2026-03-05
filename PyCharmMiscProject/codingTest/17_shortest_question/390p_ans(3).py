from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [-1]*(n+1)
distance[1] = 0
q = deque([1])

while q:
    x = q.popleft()
    for i in graph[x]:
        if distance[i] == -1:
            distance[i] = distance[x]+1
            q.append(i)

max_distance = max(distance)
candidates = [i for i in range(1,n+1) if distance[i] == max_distance]
print(candidates[0], max_distance, len(candidates))















