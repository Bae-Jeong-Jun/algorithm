n = int(input())
result = 0

# 풀이과정 1
# while n >= 0:
#     if n % 5 == 0:
#         result += n // 5
#         print(result)
#         break
#     else:
#         n -= 3
#         result += 1
# else:
#     print(-1)

# 풀이과정 2
result2 = -1
for i in range(n//5,-1,-1):
    if (n-i*5)%3 == 0:
        result2 = i + (n-i*5)//3
        break

print(result2)