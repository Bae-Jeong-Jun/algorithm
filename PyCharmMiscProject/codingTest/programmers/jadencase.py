# def solution(s):
#     newS = list(s.split())
#
#     for i in range(len(newS)):
#         newS[i] = newS[i].capitalize()
#
#     return " ".join(newS)

def solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])


s = input()

print(solution(s))

