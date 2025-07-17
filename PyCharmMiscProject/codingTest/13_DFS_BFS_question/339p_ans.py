# 모든 거리는 1이라는 조건 -> 너비 우선 탐색 이용
# 시간 복잡도 O(N+M)

from collections import deque

n, m, k, x= map(int, input().split())

data= [[] for _ in range(n+1)]

# a, b 사이 단방향 도로 존재
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0
q = deque([])
q.append(x)

while q:
    now = q.popleft()
    for next_node in data[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)







