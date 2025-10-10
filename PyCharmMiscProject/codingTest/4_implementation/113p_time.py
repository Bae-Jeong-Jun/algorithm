n = int(input())

# 분과 초 중에 n 이 들어가는 횟수
count = 0
for i in range(60):
    if str(n) in str(i):
        count +=1

# 시 중에 n 이 들어가는 횟수
count2 = 0
for j in range(n+1):
    if str(n) in str(j):
        count2 +=1

print(count)
print(count2)
total = (n+1) * 60 * 60
minus = (n+1 - count2)*(60-count)*(60-count)
result = total-minus

# 전체 경우에서 n이 안들어가는 경우의 수 뺌
print(result)

# 시간 복잡도 : 60+(n+1)