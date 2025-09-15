words = list(input().split())
queries = list(input().split())
result = []

for query in queries:
    count = 0
    length = len(query)
    for word in words:
        check = 0
        if len(word) == len(query):
            for i in range(length):
                if query[i] == word[i] or query[i] == "?":
                    check += 1
        if check == length:
            count += 1
    result.append(count)

print(result)