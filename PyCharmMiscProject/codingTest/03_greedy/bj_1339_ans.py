n = int(input())
data = [input() for _ in range(n)]

checked = [0]*26
for words in data:
    for i in range(len(words)):
        position = ord(words[i])-ord('A')
        checked[position] += 10**(len(words)-1-i)

alphabet = [(weight, i) for i, weight in enumerate(checked)]
alphabet.sort(reverse=True)

result = 0
number = 9
for weight, i in alphabet:
    if weight == 0:
        break
    result += weight*number
    number -= 1

print(result)