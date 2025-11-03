n = int(input())

data = [[]for _ in range(101)]

for i in range(n):
    name, score = input().split()
    score = int(score)
    data[score].append(name)

for i in range(101):
    for name in data[i]:
        print(name, end =" ")