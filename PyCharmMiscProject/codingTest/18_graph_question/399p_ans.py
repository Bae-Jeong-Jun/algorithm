from collections import deque

t = int(input()) # 테스트 케이스 갯수
for _ in range(t):
    n = int(input()) # 2 <= 팀의 수 <= 500
    last = list(map(int,input().split())) # 작년 등수

    graph = list([False]*(n+1) for _ in range(n+1))
    indegree = [0]*(n+1)

    # 작년 순위로 그래프 만들기
    for i in range(n):
        for j in range(i+1, n):
            higher = last[i]
            lower = last[j]
            graph[higher][lower] = True
            indegree[lower] += 1

    m = int(input())  # 등수 바뀐 쌍의 수
    for _ in range(m):
        a,b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[b] += 1
            indegree[a] -= 1

    q = deque()
    result = []
    cycle = False
    certain = True

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    for _ in range(n):
        if not q:
            cycle = True
            break
        if len(q) > 1:
            certain = False

        now = q.popleft()
        result.append(now)

        for i in range(1,n+1):
            if graph[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        print(" ".join(map(str,result)))
