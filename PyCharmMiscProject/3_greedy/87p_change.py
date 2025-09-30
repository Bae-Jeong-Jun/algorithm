n = int(input())

a = n // 500
b = (n % 500) // 100
c = (n % 100) // 50
d = ((n % 100) % 50) // 10

result = a+b+c+d

print(result)