# n : 볼링공 갯수
# m : 공의 최대 무게
n, m = map(int, input().split())

li = list(input().split())
li = li[:n]

result = 0
for i in range(len(li)):
    for j in range(i, len(li)):
        if li[i] != li[j] :
            result +=1
        else:
            continue

print(result)