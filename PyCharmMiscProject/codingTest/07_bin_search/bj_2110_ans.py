def can_place(dist):
    sum = 1
    last_pos = data[0]
    for i in range(1, n):
        if data[i] - last_pos >= dist:
            sum += 1
            last_pos = data[i]
        if sum == c:
            return True
    return False


n, c = map(int, input().split())
data = [int(input()) for _ in range(n)]
data.sort()

left = 1
right = data[-1] - data[0]
answer = 0

while left <= right:
    mid = (left + right) // 2
    if can_place(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)