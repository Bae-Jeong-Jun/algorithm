n = int(input())

count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if (str(n) in str(i)) or (str(n) in str(j)) or (str(n) in str(k)):
                count += 1

print(count)

# 시간 복잡도 : (n+1)*60*60*3