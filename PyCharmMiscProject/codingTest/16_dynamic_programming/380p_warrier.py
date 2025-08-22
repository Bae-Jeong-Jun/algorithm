# 1 <= n <= 2000
n = int(input())
data = list(map(int, (input().split())))
data = data[:n]

def check(data, x, y):
    for i in range(x, y):
        for j in range(x+1, y):
            if data[i] < data[j]:
                data.pop(i)
                return check(data, i, len(data))

check(data, 0, n)
print(data)
print(n - len(data))

