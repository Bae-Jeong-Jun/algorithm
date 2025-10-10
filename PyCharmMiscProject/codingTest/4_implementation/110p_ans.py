n = int(input())
data = list(input().split())
x, y = 1, 1

# 상,하,좌,우
move = ["U","D","L","R"]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for d in data:
    for m in range(len(move)):
        if d == move[m]:
            nx = x + dx[m]
            ny = y + dy[m]
    if 1 <= nx <= n and 1 <= ny <= n:
        x,y = nx,ny

print(x,y)