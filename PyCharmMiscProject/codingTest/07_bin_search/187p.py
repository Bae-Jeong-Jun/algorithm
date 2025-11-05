# 순차 탐색. 시간 복잡도 : O(N)
# 생성할 원소 갯수, 찾을 문자열
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i

n, data = input().split()
n = int(n)

# 원소 갯수 만큼 문자열 입력
array = input().split()
result = sequential_search(n, data, array)
print(result)