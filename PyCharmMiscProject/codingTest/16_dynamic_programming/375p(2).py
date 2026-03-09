import copy

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    gold = []
    dx = [-1,0,1]

    for i in range(n):
        gold.append(data[i*m:i*m+m])

    total_gold = copy.deepcopy(gold)
    for a in range(n):
        for b in range(1,m):
            total_gold[a][b] = -1

    for j in range(m):
        for k in range(n):
            now = total_gold[k][j]
            for l in range(3):
                nx = k + dx[l]
                ny = j + 1
                if 0<=nx<n and 0<=ny<m:
                    nxt = now + gold[nx][ny]
                    total_gold[nx][ny] = max(total_gold[nx][ny], nxt)

    answer = 0
    for c in range(n):
        answer = max(total_gold[c][m-1], answer)
    print(answer)
