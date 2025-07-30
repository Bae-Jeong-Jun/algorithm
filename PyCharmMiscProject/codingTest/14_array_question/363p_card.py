n = int(input()) # 1 <= n <= 100000
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()

sum = 0
answer = 0
for i in range(n):
    sum += data[i]
    answer += sum
print(answer-data[0])