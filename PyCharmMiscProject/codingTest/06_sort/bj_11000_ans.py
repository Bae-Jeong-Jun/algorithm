import heapq
import sys
input = sys.stdin.readline

n = int(input())
lectures = []
for _ in range(n):
    s, e = map(int, input().split())
    lectures.append((s,e))

lectures.sort()
heap = []
a,b = lectures[0]
heapq.heappush(heap, b) # 첫 강의 끝나는 시간 넣기

for i in range(1,n):
    start, end = lectures[i]
    if start >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

print(len(heap))