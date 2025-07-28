# itertools 사용
from itertools import combinations

n, m = map(int, input().split())

# 도시 정보
# 0: 빈칸, 1 : 집, 2 : 치킨집
data = []
home = []
chicken = []
selected = [] # 선택된 치킨집

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            home.append((i,j))
        elif data[j] == 2:
            chicken.append((i, j))

candidates = list(combinations(chicken, m))

def get_sum(candidate):
    chicken_distance = 0
    for idx in home:
        temp = 1e9
        hx, hy = idx
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        chicken_distance += temp
    return chicken_distance

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)





