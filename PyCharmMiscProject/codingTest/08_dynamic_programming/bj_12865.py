# n : 물품의 수
# k : 버틸 수 있는 무게
n, k = map(int, input().split())

data = []
for _ in range(n):
    w, v = map(int,input().split())
    data.append((w,v))

# ex : 가방에 든 물건 무게 2kg 일때 최대 value
d = [0]*(k+1)

for dw, dv in data:
    for weight in range(k, dw-1, -1):
        d[weight] = max(d[weight], d[weight-dw] + dv)

print(d[k])
