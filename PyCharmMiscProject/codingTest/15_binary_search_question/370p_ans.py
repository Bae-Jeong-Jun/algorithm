from bisect import bisect_left, bisect_right

words = list(input().split())
queries = list(input().split())

def count_by_range(array, left, right):
    return bisect_right(array, right) - bisect_left(array, left)

def solution(words, queries):
    words_by_len = {}
    rev_words_by_len = {}

    for word in words:
        l = len(word)
        if l not in words_by_len:
            words_by_len[l] = []
            rev_words_by_len[l] = []
        words_by_len[l].append(word)
        rev_words_by_len[l].append(word[::-1]) # 단어 뒤집어서 저장

    # 길이별 정렬
    for l in words_by_len:
        words_by_len[l].sort()
        rev_words_by_len[l].sort()

    result = []
    for query in queries:
        l = len(query)
        if len(query) not in words_by_len:
            result.append(0)
            continue

        # ex) fro??
        if query[0] != "?":
            left = query.replace("?","a")
            right = query.replace("?","z")
            result.append(count_by_range(words_by_len[l], left, right))
        # ex) ??ont
        else:
            rev_query = query[::-1]
            left = rev_query.replace("?","a")
            right = rev_query.replace("?", "z")
            result.append(count_by_range(rev_words_by_len[l], left, right))

    return result

print(solution(words, queries))







