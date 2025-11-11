# 파라메트릭 서치 유형 : 범위 내에서 조건을 만족하는 가장 큰 값 찾기

def bin_search(array, start, end, num):
    if start > end:
        return end
    else:
        mid = (start+end) // 2
        cutted = 0
        for a in array:
            if a - mid > 0:
                cutted += a - mid
        if cutted >= num:
            return bin_search(array, mid+1, end, num)
        else:
            return bin_search(array, start, mid-1, num)

# n : 떡의 갯수, m : 요청한 길이
n, m = map(int, input().split())
tteok = list(map(int, input().split()))

max_length = max(tteok)
li = [0]*(max_length+1)
for i in range(n):
    li[tteok[i]] += 1

sorted_tteok = []
for j in range(max_length+1):
    if li[j] != 0:
        for k in range(li[j]):
            sorted_tteok.append(j)

result = bin_search(sorted_tteok, 0, max_length, m)
print(result)







