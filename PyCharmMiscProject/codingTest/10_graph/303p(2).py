from collections import deque
import copy

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for j in graph[now]:
            indegree[j] -= 1
            result[j] = max(result[j], result[now] + time[j])
            if indegree[j] == 0:
                q.append(j)

    for i in range(1,n+1):
        print(result[i])

n = int(input())
time = [0]*(n+1)
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    data = list(map(int,input().split()))
    time[i] = data[0]
    for j in data[1:-1]:
        indegree[i] += 1
        graph[j].append(i) # 연결된 다음 강좌 담기

topology_sort()