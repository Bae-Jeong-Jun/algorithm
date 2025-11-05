# 이진 탐색. 시간복잡도 : O(logN)
# 정렬이 돼있어야함
# 재귀함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif target > array[mid]:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

n, target = map(int, input().split())
array = list(map(int,input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소 존재 안함")
else:
    print(result)
