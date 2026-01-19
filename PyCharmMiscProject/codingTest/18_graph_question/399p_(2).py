from collections import deque

t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    n = int(input()) # 팀의수
    last = list(map(int, input().split()))
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0]*(n+1)

    for i in range(n):
        for j in range(i+1, n):
            higher = last[i]
            lower = last[j]
            graph[higher][lower] = True
            indegree[lower] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    q = deque([])
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    impossible = False
    certain = True
    for _ in range(n):
        if not q:
            impossible = True
            break
        elif len(q) > 1:
            certain = False

        now = q.popleft()
        result.append(now)
        for i in range(1, n+1):
            if graph[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    if impossible:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        print(" ".join(map(str,result)))













