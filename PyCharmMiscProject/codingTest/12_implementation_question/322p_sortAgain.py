line = (input())

value = 0
result = []

for i in range (len(line)):
    if line[i].isalpha() :
        result.append(line[i])
    else:
        value += int(line[i])

result.sort()

if value != 0:
    result.append(str(value))
print(''.join(result))
# for i in result:
#     print(i, end='')
# print(value)


