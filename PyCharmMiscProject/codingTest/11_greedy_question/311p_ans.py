n = int(input())
li = list(map(int, input().split()))

li.sort()
count = 0
result = 0

for l in li:
    count += 1
    if l <= count: # 그룹에 포함시킴
        result += 1
        count = 0

print(result)