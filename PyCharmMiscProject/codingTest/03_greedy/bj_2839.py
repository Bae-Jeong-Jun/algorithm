n = int(input())

first = n // 5
extra = n % 5
second = 0
result = 0

if first == 0:
    if extra != 3:
        result = -1
    else:
        result = 1
else:
    if extra != 0:
        while (extra % 3) != 0:
            extra += 5
            first -= 1
        if first < 0:
            result = -1
        else:
            second = extra // 3
            result = first + second
    else:
        result = first

print(result)