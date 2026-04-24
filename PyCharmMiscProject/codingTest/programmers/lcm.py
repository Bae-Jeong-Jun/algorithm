from fractions import gcd

def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer

# def solution(arr):
#     number = max(arr)
    
#     while True:
#         count = 0
#         for a in arr:
#             if number % a == 0:
#                 count += 1

#         if count == len(arr):
#             return number
#         else:
#             number += max(arr)
