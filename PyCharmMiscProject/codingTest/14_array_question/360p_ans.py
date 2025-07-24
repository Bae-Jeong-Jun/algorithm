# 파이썬 정렬 알고리즘 시간 복잡도 : O(NlogN)
n = int(input())

home = list(map(int, input().split()))
home = home[:n]
home.sort()

print(home[(n-1)//2])