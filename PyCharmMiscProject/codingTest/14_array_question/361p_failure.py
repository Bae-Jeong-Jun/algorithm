# 1 <= n(스테이지 갯수) <=500
# 1 <= stages 배열 len(stages) <= 200000
# stages n+1 은 모두 클리어한 사람
# 실패율
# : 도달했지만 클리어 못한 플레이어 / 도달한 플레이어

n = int(input())
stages = list(map(int, input().split()))

count = len(stages)
result = [0]*(n+2) # 도달했지만 클리어 못한 플레이어
countList = [0]*(n+3) # 도달한 플레이어
countList[1] = count

for i in range(1, n+2):
    for j in stages:
        if i == j:
            result[i] += 1
            count -= 1
            countList[i+1] = count
        else:
            countList[i+1] = count

answer = []
for i in range(1, n+1):
    answer.append([i, result[i] / countList[i]])

answer.sort(key=lambda x: (-x[1],x[0]))
answer = [x[0] for x in answer]

print(result)
print(countList)
print(answer)