n = int(input())
data = list(input().split())

position = [1,1]
for i in data:
    if i == "U":
        next = [position[0]-1, position[1]]
    if i == "D":
        next = [position[0]+1, position[1]]
    if i == "L":
        next = [position[0], position[1]-1]
    if i == "R":
        next = [position[0], position[1]+1]
    if 1 <= next[0] <= n and 1 <= next[1] <= n:
        position = next

print(position)