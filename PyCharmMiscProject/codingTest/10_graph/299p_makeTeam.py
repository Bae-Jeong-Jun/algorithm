# 0~N 까지의 팀
# M번 연산 가능

def union_team(parent, x, y):
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

def find_team(parent, x):
    if parent[x] != x:
        find_team(parent, parent[x])
    return parent[x]

N, M = map(int, input().split())

# 부모 정보 자기자신으로 초기화
parent = [0] * (N+1)
for n in range(N+1):
    parent[n] = n

for m in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        union_team(parent, b, c)
    elif a == 1:
        find_team(parent, b)
        find_team(parent, c)
        if find_team(parent, b) != find_team(parent, c):
            print('NO')
        else:
            print('YES')