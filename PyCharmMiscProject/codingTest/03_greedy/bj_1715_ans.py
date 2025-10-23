import heapq
n = int(input())

data = [int(input()) for _ in range(n)]
heapq.heapify(data)

result = 0
while len(data) > 1:
    first = heapq.heappop(data)
    second = heapq.heappop(data)
    cost = first+second
    result += cost

    heapq.heappush(data,cost)

print(result)
