import heapq

n = int(input()) # 1 <= n <= 100000
heap = []

for _ in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0
while len(heap) != 1:
    # 값이 작은 원소를 꺼냄
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one + two
    heapq.heappush(heap, sum_value)
    result += sum_value
print(result)