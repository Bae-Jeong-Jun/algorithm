# (a, b)
# a : 북쪽으로 떨어진 개수
# b : 서쪽으로 떨어진 개수
# d : 보는 방향
n, m = map(int, input().split())
a, b, d = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

visit = list([0]*m for _ in range(n))
visit[a][b] = 1 # 방문

# 북,동,남,서
da = [-1,0,1,0]
db = [0,1,0,-1]

def turn_left(d):
    nd = (d-1)%4
    return nd

turn_count = 0
result = 1
while True:
    d = turn_left(d)
    na = a + da[d]
    nb = b + db[d]
    if data[na][nb] == 0 and visit[na][nb] == 0:
        visit[na][nb] = 1
        a,b = na,nb
        result += 1
        turn_count = 0
        continue
    else:
        turn_count+=1

    if turn_count == 4:
        na = a - da[d]
        nb = b - db[d]
        if data[na][nb] == 1:
            break
        else:
            a = na
            b = nb
            turn_count = 0

print(result)




