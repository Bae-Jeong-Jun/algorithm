def solution(s):
    length = len(s)
    result = ''
    count = 1
    global i
    for i in range(1, length):
        if s[i] == s[i-1]:
            count += 1
        elif count == 1:
            result += s[i-1]
        else:
            result += (str(count) + s[i - 1])
            count = 1

    if count == 1:
        result += s[i]
    else:
        result += (str(count) + s[i-1])

    answer = len(result)
    return answer, result

line = input()
print(solution(line))