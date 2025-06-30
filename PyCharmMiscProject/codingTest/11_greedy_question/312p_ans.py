data = input()
result = 0

for d in range(len(data)):
    num = int(data[d])
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num

print(result)