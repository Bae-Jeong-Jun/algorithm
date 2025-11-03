# 계수 정렬
n = int(input())
data = []

for _ in range(n):
    data.append(int(input()))

length = len(data)
maximum = max(data)
count = [0]*(maximum+1)

for i in range(length):
    count[data[i]] += 1

for i in range(len(count)-1,0,-1):
    for _ in range(count[i]):
        print(i, end= " ")