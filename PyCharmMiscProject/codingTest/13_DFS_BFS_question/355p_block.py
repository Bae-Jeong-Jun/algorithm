from collections import deque
n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

def solution(board):
    def get_next(pos):
        next_pos = []
        pos = list(pos)
        (x1,y1),(x2,y2) = pos[0],pos[1]
        move = [(0,1),(0,-1),(1,0),(-1,0)]

        for dx,dy in move:
            nx1, ny1, nx2, ny2 = x1+dx, y1+dy, x2+dx, y2+dy
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
                if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                    next_pos.append({(nx1,ny1),(nx2,ny2)})

        if x1 == x2: # 가로 방향
            for d in [-1,1]:
                if 0 <= x1+d < n and 0 <= x2+d < n:
                    if board[x1+d][y1] == 0 and board[x2+d][y2] == 0:
                        next_pos.append({(x1,y1),(x1+d,y1)})
                        next_pos.append({(x2,y2),(x2+d,y2)})

        if y1 == y2: # 세로 방향
            for d in [-1,1]:
                if 0 <= y1+d < n and 0 <= y2+d < n:
                    if board[x1][y1+d] == 0 and board[x2][y2+d] == 0:
                        next_pos.append({(x1,y1),(x1,y1+d)})
                        next_pos.append({(x2,y2),(x2,y2+d)})

        return next_pos


    q = deque()
    visited = []
    start = {(0,0), (0,1)}
    q.append((start, 0))
    visited.append(start)

    while q:
        pos, cost = q.popleft()
        if (n-1, n-1) in pos:
            return cost
        for next_pos in get_next(pos):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)

    return -1 # 도달 불가능

print(solution(board))






