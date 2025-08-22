# 1 <= n <= 2000
n = int(input())
data = list(map(int, (input().split())))
data = data[:n]
data.reverse()

# i 번째 원소를 마지막으로 하는 수열 길이
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
print(n-max(dp))