n, m ,k = map(int, input().split())
data = list(map(int,input().split()))
data = data[:n]

data = sorted(data, reverse=True)

result = 0
count = 0

while count < m:
    for _ in range(k):
        if count == m:
            break
        result += data[0]
        count += 1
    if count == m:
        break
    result += data[1]
    count += 1

print(data)
print(result)