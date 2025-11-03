n = int(input())

data = []
for _ in range(n):
    data.append(input().split())

data.sort(key = lambda x: x[1])

for i in range(n):
    print(data[i][0], end = " ")