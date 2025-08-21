from itertools import permutations

n = int(input())
weak = input().split()
dist = input().split()

length = len(weak)
for i in range(length):
    weak[i] = int(weak[i])
    weak.append(weak[i]+n)

for i in range(len(dist)):
    dist[i] = int(dist[i])

answer = len(dist) + 1
for start in range(length):
    for friends in list(permutations(dist, len(dist))):
        count = 1
        position =  weak[start] + friends[count-1]
        for index in range(start, start+length):
            if weak[index] > position:
                count += 1
                if count > len(dist):
                    break
                position = weak[index] + friends[count-1]
        answer = min(answer, count)

if answer > len(dist):
    print(-1)
else:
    print(answer)











