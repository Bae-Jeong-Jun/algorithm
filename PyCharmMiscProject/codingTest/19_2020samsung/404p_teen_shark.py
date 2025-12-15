import heapq
import copy
data=[]
q = []

for i in range(4):
    line = list(map(int, input().split()))
    data_line = []
    for j in range(0,8,2):
        data_line.append((line[j], line[j+1]))
        heapq.heappush(q,(line[j], line[j+1], i, j//2))
    data.append(data_line)

result = 0
num, dir = data[0][0]

shark = [0,0,0]
data[0][0] = (0,0)
shark[2] = dir
result += num

copy_q = copy.deepcopy(q)
while copy_q:
    h_num, h_dir, h_x, h_y = heapq.heappop(copy_q)
    if num == h_num:
        q.pop(h_num-1)


