from bisect import bisect_left, bisect_right

def count_by_range(data, left_value, right_value):
    index_left = bisect_left(data, left_value)
    index_right = bisect_right(data, right_value)
    result = index_right - index_left
    return result

n, x = map(int, input().split())
data = list(map(int, input().split()))
data = data[:n]
data.sort()  # 이진 탐색을 위해 반드시 정렬 필요

# 값이 [x,x] 범위에 있는 데이터 갯수 계산
count = count_by_range(data,x,x)

if count == 0:
    print(-1)
else:
    print(count)
