from collections import deque
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for d in data:
    if d > target:
        break
    else:
        target += d

print(target)