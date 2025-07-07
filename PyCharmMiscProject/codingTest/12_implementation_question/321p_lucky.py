n = list(map(int, input()))

left = 0
for i in range(len(n)//2):
    left += n[i]

right = 0
for j in range(len(n)//2, len(n)):
    right += n[j]

if left == right:
    print("LUCKY")
else:
    print("READY")
