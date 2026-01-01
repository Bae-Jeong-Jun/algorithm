n = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0

for i in range(n):
    left = 0
    right = n - 1
    target = data[i]
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        s = data[left] + data[right]
        if target == s:
            result += 1
            break
        elif target > s:
            left += 1
        else:
            right -= 1

print(result)