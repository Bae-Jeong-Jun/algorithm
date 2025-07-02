# n : 볼링공 갯수
# m : 공의 최대 무게
# li : 볼링공 각각의 무게
n, m = map(int, input().split())
li = list(map(int, input().split()))
li = li[:n]

# 볼링공 무게 1~10 각각의 갯수 저장
array = [0] * 11
for l in li:
    array[l] += 1

result = 0
for a in range(1, m+1):
    # 한명이 a 무게를 골랐을 때 다른 한명은 다른 무게를 고름
    n -= array[a]
    result += array[a] * n

print(result)