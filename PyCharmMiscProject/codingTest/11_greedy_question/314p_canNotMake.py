# 동전의 갯수
N = int(input())

# 동전의 종류
coin = list(map(int, input().split()))
coin = coin[:N]
coin.sort()

target = 1
result = 0
for c in coin:
    if target < c:
        result = target
    else:
        target += c

print(result)
