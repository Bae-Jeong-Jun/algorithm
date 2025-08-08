def bin_search(data, start, end):
    if start > end:
        return None
    else:
        mid = (start + end) // 2
        if mid == data[mid]:
            return mid
        elif mid < data[mid]:
            return bin_search(data, start, mid-1)
        else:
            return bin_search(data, mid+1, end)

n = int(input())
data = list(map(int, input().split()))
index = bin_search(data, 0, n-1)

if index == None:
    print(-1)
else:
    print(index)
