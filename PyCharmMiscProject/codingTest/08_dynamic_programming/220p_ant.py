n = int(input())
data = list(map(int, input().split()))

d = [0]*101
# d[창고 갯수]
d[1] = data[0]
d[2] = max(data[0],data[1])
# d[3] = max(d[2], d[1] + data[2])
# d[4] = max(d[3], d[2] + data[3])
# d[5] = max(d[4], d[3] + data[4])

for i in range(3, n+1):
    d[i] = max(d[i-1], d[i-2] + data[i-1])

print(d[n])
