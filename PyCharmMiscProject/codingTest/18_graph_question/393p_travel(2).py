# n : 여행지 수, m : 여행 계획 된 도시 수
def union_parents(parents,x,y):
    x = find_parents(parents,x)
    y = find_parents(parents,y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x

def find_parents(parents,z):
    if parents[z] != z:
        parents[z] = find_parents(parents,parents[z])
    return parents[z]

n, m = map(int, input().split())
parents = [0]*(n+1)
for i in range(1,n+1):
    parents[i] = i

for i in range(1,n+1):
    data = [0]+list(map(int, input().split()))
    for j in range(i+1,n+1): # 중복 방지
        if data[j] == 1:
            union_parents(parents,i,j)

plans = list(map(int, input().split()))
result = True

for i in range(m-1):
    if find_parents(parents,plans[i]) != find_parents(parents,plans[i+1]):
        result = False
        break

if result:
    print('YES')
else:
    print('NO')













