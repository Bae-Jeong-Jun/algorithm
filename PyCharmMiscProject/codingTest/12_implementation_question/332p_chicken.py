# itertools 없이 구현
# n : 도시의 크기 2<=n<=50
# m : 살릴 치킨집 갯수 1<=m<=13
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

def cal_distance():
    sum_distance = 0
    for idx in home:
        chicken_distance = 1e9
        hx, hy = idx
        for j in selected:
            cx, cy = chicken[j]
            temp = abs(hx - cx) + abs(hy - cy)
            chicken_distance = min(chicken_distance, temp)
        sum_distance += chicken_distance
    return sum_distance

result = 1e9
def dfs(start, depth):
    global result
    if depth == m:
        result = min(result, cal_distance())
        return
    for i in range(start, len(chicken)):
        selected.append(i)
        dfs(i+1, depth+1)
        selected.pop()

dfs(0, 0)
print(result)