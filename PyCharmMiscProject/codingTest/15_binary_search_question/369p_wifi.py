# 2 <= c(공유기 갯수) <= n(집의 갯수) <= 200000
# 공유기 사이의 거리가 최대한 클 것
n, c = map(int, input().split())

# 집 번호 저장
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

start = 1 # 집 간 거리의 최소값
end = data[-1] - data[0] # 집 간 거리의 최대값
result = 0

while start <= end:
    mid = (start + end) // 2 # 공유기 사이의 거리
    value = data[0]
    count = 1

    for i in range(1, n):
        if data[i] >= value + mid:
            value = data[i]
            count += 1

    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)