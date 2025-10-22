n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=False)

result = 0
total = 0
for d in data:
    result += d
    total += result

print(total)