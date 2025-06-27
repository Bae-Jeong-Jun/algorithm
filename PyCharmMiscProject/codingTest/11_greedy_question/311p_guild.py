# N 명의 모험가
N = int(input())

# 공포도 X인 사람은 X명 이상 참여
li = list(map(int, input().split()))

result = 0
while len(li) > 0 and max(li) <= len(li):
    x = max(li)
    li.pop(li.index(x))
    for _ in range(x-1):
        y = max(li)
        li.pop(li.index(y))
    result += 1

while len(li) > 0 and min(li) == 1:
    z = min(li)
    li.pop(li.index(z))
    result += 1

print(li)
print(result)
