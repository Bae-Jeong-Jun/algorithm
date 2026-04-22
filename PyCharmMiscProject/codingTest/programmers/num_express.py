def solution(n):
    answer = 0
    numsum = 0
    
    for i in range(1,n+1):
        numsum = 0
        for j in range(i,n+1):
            numsum += j
            if numsum == n:
                answer += 1
                break
            if numsum > n:
                break
    
    return answer
