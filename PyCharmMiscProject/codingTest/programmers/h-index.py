# def solution(citations):
#     answer = 0
    
#     for i in range(len(citations)+1):
#         count = 0
#         for c in citations:
#             if c >= i:
#                 count +=1
#         if count >= i:
#                 answer = i
                
#     return answer

def solution(citations):
    citations.sort(reverse=True)
    
    for i, c in enumerate(citations):
        if c < i + 1:
            return i
    
    return len(citations)











