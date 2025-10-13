data = input() # a1
hor = ord(data[0]) - ord("a")+1
ver = int(data[1])

steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

count = 0
for step in steps:
    nh = hor + step[0]
    nv = ver + step[1]
    if 1 <= nh <= 8 and 1 <= nv <= 8:
        count += 1

print(count)