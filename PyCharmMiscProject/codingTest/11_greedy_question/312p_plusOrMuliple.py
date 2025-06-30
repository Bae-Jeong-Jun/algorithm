num = str(input())
li = []

for l in range(len(num)):
    li.append(int(num[l:l+1]))

# 풀이 1
result = li[0]
for l in range(1, len(li)):
    if result in(0, 1) or li[l] in(0,1) :
        result += li[l]
    else:
        result *= li[l]
print(result)

# 풀이 2
result = 0
for l in range(len(li)):
    if result in(0, 1) or li[l] in(0,1) :
        result += li[l]
    else:
        result *= li[l]
print(result)
