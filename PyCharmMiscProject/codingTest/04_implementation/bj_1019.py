n = int(input())

data = [0]*10

for i in range(1,n+1):
    nums = str(i)
    for num in nums:
        data[int(num)] += 1

for d in data:
    print(d, end=" ")