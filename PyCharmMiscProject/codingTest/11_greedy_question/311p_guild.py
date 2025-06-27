# N 명의 모험가
N = int(input())

# 공포도 X인 사람은 X명 이상 참여
li = list(map(int, input().split()))

result = 0
while len(li):
    m = max(li)
    if m != 1:
        li.pop(li.index(m))
        for _ in range(m-1):
            n = max(li)
            li.pop(li.index(n))
        result += 1
    else:
        li.pop(li.index(m))
        result += 1

print(result)
