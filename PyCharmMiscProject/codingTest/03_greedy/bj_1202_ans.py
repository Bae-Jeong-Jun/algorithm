import heapq
# n : 보석 갯수, k : 가방 갯수
# m, v : 보석 무게, 보석 가격
# c : 가방에 담을 수 있는 최대 무게
n, k = map(int, input().split())

jewels= []
for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((m,v))

bags = []
for _ in range(k):
    bags.append(int(input()))

jewels.sort()
bags.sort()

result = 0
queue = []
idx = 0

for bag in bags:
    while idx < n and jewels[idx][0] <= bag:
        heapq.heappush(queue,-jewels[idx][1])
        idx += 1
    if queue:
        result += -heapq.heappop(queue)

print(result)

# 시간 복잡도
# 정렬 : O(nlogn +klogk)
# 가방순회 : O(k)
# heap 삽입/삭제 : O(logn)
# => 총 시간 복잡도 : O((n+k)log(n))








