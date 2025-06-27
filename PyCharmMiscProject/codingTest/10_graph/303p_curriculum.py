from collections import deque
import copy

# N : 듣고자 하는 강의 수
N = int(input())

# 진입 차수 0으로 초기화
indegree = [0] * (N+1)

# 강의 시간 정보
time = [0] * (N+1)

# graph에 선수 강의 정보 저장
graph = [[] for n in range(N+1)]

for n in range(1, N+1):
    data = list(map(int, input().split()))
    time[n] = data[0]
    for x in data[1:-1]:
        graph[x].append(n)
        indegree[n] += 1

queue = deque()
result = copy.deepcopy(time)
# 우선 진입 차수 0인 노드 삽입
for n in range(1, N+1):
    if indegree[n] == 0:
        queue.append(n)

while queue:
    now = queue.popleft()
    for x in graph[now]:
        result[x] = max(result[x], result[now] + time[x])
        indegree[x] -= 1
        if indegree[x] == 0:
            queue.append(x)

for n in range(1, N+1):
    print(result[n])










