data = input() # a1
hor = ord(data[0]) # ord(a)
ver = int(data[1]) # 1

first = [2,2,-2,-2]
second = [1,-1,1,-1]

count = 0
# 수평 2칸 수직 1칸
for i in range(4):
    nh = hor+first[i]
    nv = ver+second[i]
    if ord("a") <= nh <= ord("h") and 1<=nv<=8:
        count += 1

# 수직 2칸 수평 1칸
for i in range(4):
    nv = ver+first[i]
    nh = hor+second[i]
    if ord("a") <= nh <= ord("h") and 1<=nv<=8:
        count += 1

print(count)
