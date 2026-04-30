def solution(n):
    answer = n
    ncount = format(n,'b').count('1')
    
    while True:
        answer += 1
        acount = (bin(answer)[2:]).count('1')
    
        if ncount == acount:
            return answer
