start = 0
n,m= 2,2
data = [1,2,5,7,5,3,2,2,3,2,3,2]
dp = []
for i in range(n):
    dp.append(list(data[start:start+m]))
    start += m
print(dp)

