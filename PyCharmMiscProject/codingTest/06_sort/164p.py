# 삽입 정렬 O(n^2)
# 이미 정렬된 상태라면 빠르게 동작함
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print(array)