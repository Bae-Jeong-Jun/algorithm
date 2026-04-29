def solution(s):
    iteration, count = 0, 0
    while s != '1':
        iteration += 1
        count += s.count('0')
        s = bin(s.count('1'))[2:]
    return [iteration, count]

# def solution(s):
#     count_0 = 0
#     change = 0
#     while True:
#         if s == "1":
#             break
            
#         li = list(map(int, s))

#         count_1 = 0
#         for x in li:
#             if x == 0:
#                 count_0 += 1
#             elif x == 1:
#                 count_1 += 1

#         s = format(count_1, 'b')
#         change += 1
        
#     return [change, count_0]



