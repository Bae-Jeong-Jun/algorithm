n = int(input())

home = list(map(int, input().split()))
home = home[:n]

location = 0
sumDistance = 1e9
for i in home:
    result = 0
    for j in home:
        if i != j:
            if i > j:
                result += (i - j)
            else:
                result += (j - i)
    if sumDistance > result:
        sumDistance = result
        location = i

print("거리 총합 : ",sumDistance)
print("안테나 위치 : ",location)