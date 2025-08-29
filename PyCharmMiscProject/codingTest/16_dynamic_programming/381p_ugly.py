n = int(input())

count = 0
original_num = 1
data = []
while count != n:
    num = original_num
    while num % 2 == 0:
        num = num / 2
    while num % 3 == 0:
        num = num / 3
    while num % 5 == 0:
        num = num / 5

    if num == 1:
        data.append(original_num)
        count += 1
    original_num += 1

print(data)
print(data[n-1])