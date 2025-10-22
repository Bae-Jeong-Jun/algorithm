n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

data.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0
for s, e in data:
    if s >= end_time:
        end_time = e
        count += 1

print(count)