# 계수 정렬
# 모든 데이터가 양의 정수이고 데이터 개수 N, 데이터 최댓값 K
# 시간 복잡도 : O(N+K)

# (가장 큰 데이터 - 가장 작은 데이터) <= 1000000
# 중복된 데이터가 많을 때
# 일 때 효율적

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

print(count)
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")