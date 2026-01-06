import sys
input = sys.stdin.readline

g = int(input()) # 탑승구의 수
p = int(input()) # 비행기의 수

def find_parents(parents,x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union_parents(parents,x,y):
    x = find_parents(parents,x)
    y = find_parents(parents,y)

    if x > y:
        parents[x] = y
    else:
        parents[y] = x

parents = [0] * (g+1)
for i in range(1,g+1):
    parents[i] = i

result = 0
for _ in range(p):
    data = find_parents(parents, int(input()))
    if data == 0:
        break
    union_parents(parents,data,data-1)
    result += 1

print(result)
