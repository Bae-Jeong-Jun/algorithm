n = int(input())
data=[]

for _ in range(n):
    line = input()
    data.append(line)

checked = [0]*26
for i in range(n):
    s = data[i]
    for j in range(len(s)):
        pos = ord(s[j])-ord('A')
        checked[pos] += 10**(len(s)-j-1)

print(checked)
checked.sort(reverse = True)
result = 0
number = 9
for i in range(len(checked)):
    if checked[i] > 0:
        result += checked[i] * number
        number -= 1

print(result)


