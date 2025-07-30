# 시간 복잡도 O(n*스테이지 수)
n = int(input())
stages = list(map(int, input().split()))

length = len(stages)
answer = []
for i in range(1, n+1):
    count = stages.count(i)

    if length == 0:
        fail = 0
    else:
        fail = count / length
    answer.append([i, fail])
    length -= count

answer.sort(key = lambda x: x[1], reverse=True)
print([x[0] for x in answer])

# counter 사용하면 O(N+M logM) M = 스테이지 수
# list 내 각 요소의 갯수 dict 형식으로 저장
from collections import Counter
n = int(input())
stages = list(map(int, input().split()))

stage_counter = Counter(stages)
length = len(stages)
answer = []
for i in range(1, n+1):
    count = stage_counter[i]

    if length == 0:
        fail = 0
    else:
        fail = count / length
    answer.append([i, fail])
    length -= count

answer.sort(key = lambda x: x[1], reverse=True)
print([x[0] for x in answer])

