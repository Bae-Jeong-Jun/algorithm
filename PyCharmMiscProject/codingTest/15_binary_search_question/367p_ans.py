n, x = map(int, input().split())
data = list(map(int, input().split()))
data = data[:n]
data.sort()  # 이진 탐색을 위해 반드시 정렬 필요

def first(data, x):
    start, end = 0, len(data)
    while start < end:
        mid = (start + end) // 2
        if data[mid] >= x:
            end = mid
        else:
            start = mid + 1
    return start

def last(data, x):
    start, end = 0, len(data)
    while start < end:
        mid = (start + end) // 2
        if data[mid] > x:
            end = mid
        else:
            start = mid + 1
    return start

left = first(data, x)
right = last(data, x)
result = right - left

print(result if result > 0 else -1)
