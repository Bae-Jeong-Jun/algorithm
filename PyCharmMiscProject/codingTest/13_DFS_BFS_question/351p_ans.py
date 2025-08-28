from itertools import combinations

def watch(x, y, d, board):
    while True:
        x += dx[d]
        y += dy[d]
        if not (0 <= x < n and 0 <= y < n):
            return True
        if board[x][y] == "O":
            return True
        if board[x][y] == "S":
            return False

def safe(board):
    for t in teacher:
        x, y = t
        for d in range(4):
            if not watch(x,y,d,board):
                return False
    return True

n = int(input())

data=[]
for i in range(n):
    data.append(input().split())

teacher = []
empty = []
for i in range(n):
    for j in range(n):
        if data[i][j] == "T":
            teacher.append((i,j))
        if data[i][j] == "X":
            empty.append((i,j))
# 상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = "No"
for objects in combinations(empty, 3):
    temp = [row[:] for row in data]
    for x, y in objects:
        temp[x][y] = "O"

    if safe(temp):
        answer = "Yes"
        break

print(answer)




