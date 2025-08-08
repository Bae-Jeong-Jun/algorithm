n = int(input())

data = list(map(int, input().split()))
count = 0
for i in range(n):
    if data[i] == i:
        print(i)
        count += 1
        break
if count == 0:
    print('-1')