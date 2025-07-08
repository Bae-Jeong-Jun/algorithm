def solution(s):
    # 1 ~ 문자열의 절반 까지 step
    answer = len(s)
    for step in range(1, len(s)//2 + 1):
        prev = s[0:step]
        count = 1
        compressed = ''
        for i in range(step, len(s), step):
            if prev == s[i:i+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[i:i + step]
                count = 1
            # elif count == 1:
            #     compressed += prev
            #     prev = s[i:i + step]
            # else:
            #     compressed += (str(count)+prev)
            #     count = 1
            #     prev = s[i:i+step]
        # 남은 문자열
        if count == 1:
            compressed += prev
        else:
            compressed += (str(count) + prev)

        print(compressed, len(compressed))
        answer = min(answer, len(compressed))
    return answer

line = input()
print(solution(line))