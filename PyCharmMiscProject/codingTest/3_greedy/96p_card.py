n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    data = data[:m]
    check = min(data)
    if check > result:
        result = check
    # result = max(result, check)

print(result)

