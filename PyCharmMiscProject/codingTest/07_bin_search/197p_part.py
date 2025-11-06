# 시간복잡도 : O((m+n)*logn)
# 정렬 n*logn
# 이진 탐색 m*logn
def bin_search(array, num, start, end):
    if start <= end:
        mid = (start + end) // 2
        if array[mid] == num:
            return True
        elif array[mid] > num:
            return bin_search(array, num, start, mid-1)
        elif array[mid] < num:
            return bin_search(array, num, mid+1, end)
    return False

n = int(input())
data = list(map(int, input().split()))
data.sort()

m = int(input())
check = list(map(int, input().split()))

for c in check:
    if bin_search(data, c, 0, len(data)):
        print('yes', end=" ")
    else:
        print('no', end=" ")