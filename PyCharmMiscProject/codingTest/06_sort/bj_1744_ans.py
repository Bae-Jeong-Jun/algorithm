n = int(input())

plus = []
minus = []
zero = 0
one = 0

for i in range(n):
    number = int(input())
    if number > 1:
        plus.append(number)
    elif number == 1:
        one += 1
    elif number == 0:
        zero += 1
    else:
        minus.append(number)

plus.sort(reverse = True)
minus.sort()

result = 0
for p in range(0,len(plus),2):
    if p+1 == len(plus):
        result += plus[p]
    else:
        result += plus[p]*plus[p+1]

for m in range(0,len(minus),2):
    if m+1 == len(minus):
        if zero > 0:
            break
        else:
            result += minus[m]
    else:
        result += minus[m]*minus[m+1]

result += one

print(result)








