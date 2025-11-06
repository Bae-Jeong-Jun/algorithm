# 계수 정렬
n = int(input())
data = list(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

array = [0]*1000001

for i in data:
    array[i] = 1

for c in check:
    if array[c] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')