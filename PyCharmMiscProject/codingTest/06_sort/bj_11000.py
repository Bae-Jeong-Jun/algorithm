n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

data.sort()

check = []
answer = 1
for d in data:
    start, end = d[0], d[1]
    if len(check) >= 1:
        plus = False
        for c in check:
            if start == c:
                break
            else:
                plus = True
        if plus:
            answer += 1
    check.append(end)

print(answer)