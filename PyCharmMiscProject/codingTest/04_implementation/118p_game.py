# (a, b)
# a : 북쪽으로 떨어진 개수
# b : 서쪽으로 떨어진 개수
# d : 보는 방향

def check(a,b,d,count):
    # 북,동,남,서
    da = [-1, 0, 1, 0]
    db = [0, 1, 0, -1]
    if count == 4:
        na = a -da[d]
        nb = b -db[d]
        if data[na][nb] == 1:
            return
        return check(na,nb,d,0)
    nd = (d - 1) % 4
    na = a + da[d]
    nb = b + db[d]

    if data[na][nb] == 1 or visit[na][nb] == 1:
        count += 1
        return check(a,b,nd,count)
    else:
        visit[na][nb] = 1
        return check(na,nb,nd,0)

n, m = map(int, input().split())
a, b, d = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

visit = list([0]*m for _ in range(n))
visit[a][b] = 1 # 방문

check(a,b,d,0)

result = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 1:
            result += 1

print(result)

