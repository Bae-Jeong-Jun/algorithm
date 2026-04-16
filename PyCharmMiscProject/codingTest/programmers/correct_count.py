def solution(s):
    left, right = 0,0
    for i in range(len(s)):
        if s[i] == "(":
            left += 1
        else:
            right += 1
        if left < right:
            return False
   
    return left == right
