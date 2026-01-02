from collections import deque

n, m = map(int, input().split())
data = [[0]*(n+1)]
for _ in range(n):
    data.append([0]+list(map(int, input().split())))
plans = list(map(int, input().split()))
visited = [False]*(n+1)

q = deque([plans[0]])
visited[plans[0]] = True

while q:
    x = q.popleft()
    for y in range(1,n+1):
        if data[x][y] == 1 and not visited[y]:
            visited[y] = True
            q.append(y)

result = True
for plan in plans:
    if not visited[plan]:
        result = False
        break

print("YES" if result else "NO")