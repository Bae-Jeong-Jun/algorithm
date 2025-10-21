n = int(input())

start = 1
end = n
digit = 1
cnt = [0]*10

while start <= end:
    while end % 10 != 9 and start <= end:
        for i in str(end):
            cnt[int(i)] += digit
        end -= 1

    while start % 10 != 0 and start <= end:
        for j in str(start):
            cnt[int(j)] += digit
        start += 1

    if start > end:
        break

    start //= 10 
    end //= 10

    count = (end-start+1)*digit

    for i in range(10):
        cnt[i] += count

    digit *= 10

for c in cnt:
    print(c, end=" ")