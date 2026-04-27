# def solution(dirs):
#     answer = 0
#     visited = set()
#     x, y = 5,5
    
#     #상하좌우
#     dx = [1,-1,0,0]
#     dy = [0,0,-1,1]
    
#     move = 0
#     for i in range(len(dirs)):
#         if dirs[i] == "U":
#             move = 0
#         elif dirs[i] == "D":
#             move = 1
#         elif dirs[i] == "L":
#             move = 2
#         elif dirs[i] == "R":
#             move = 3
#         nx, ny = x+dx[move], y+dy[move]
        
#         if 0 <= nx <=10 and 0 <= ny <= 10:
#             path1 = (x,y,nx,ny)
#             path2 = (nx,ny,x,y)
            
#             if path1 not in visited:
#                 visited.add(path1)
#                 visited.add(path2)
#                 answer += 1
#             x, y = nx, ny        
    
#     return answer

def solution(dirs):
    x, y = 0, 0
    visited = set()
    
    move_dict = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }
    
    answer = 0
    
    for d in dirs:
        dx, dy = move_dict[d]
        nx, ny = x + dx, y + dy
        
        # 좌표 범위 체크
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path1 = (x, y, nx, ny)
            path2 = (nx, ny, x, y)
            
            if path1 not in visited:
                visited.add(path1)
                visited.add(path2)
                answer += 1
            
            x, y = nx, ny
    
    return answer







