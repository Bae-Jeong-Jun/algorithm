# 시간복잡도 : O(n+m)
# set 사용하면 해시탐색
# list 사용시 O(n*m)
n = int(input())
data = set(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

for c in check:
    if c in data:
        print('yes', end=' ')
    else:
        print('no', end=' ')

