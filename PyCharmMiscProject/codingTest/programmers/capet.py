# def solution(brown, yellow):
#     if yellow == 1:
#         return [3,3]
#     else:
#         for i in range(1, yellow//2+1):
#             if yellow % i != 0:
#                 continue
#             elif (yellow // i + i)*2 + 4 == brown:
#                 return [max(yellow // i + 2, i+2), min(yellow // i + 2, i+2)]


def solution(brown, yellow):
    for h in range(1, int(yellow**0.5)+1):
        if yellow % h == 0:
            w = yellow // h
            if (w+2) * (h+2) == brown+yellow:
                return[w+2, h+2]
