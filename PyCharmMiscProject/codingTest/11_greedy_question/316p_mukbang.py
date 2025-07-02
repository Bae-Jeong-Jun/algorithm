# n : 먹는 음식의 갯수
# k : 먹방 진행한 시간
n, k = map(int, input().split())

# 각 음식을 다 먹는데 걸리는 시간
food_times = list(map(int,input().split()))
food_times = food_times[:n]

repeat = 0
def solution(food_times, y, k):
    global repeat
    for x in range(y, k):
        if repeat == n:
            return -1
        elif food_times[x % n] != 0:
                food_times[x % n] -= 1
                repeat = 0
        else:
            repeat += 1
            return solution(food_times, x+1, k+1)

    check = 0
    while food_times[k % n] == 0:
        k += 1
        check += 1
        if check == n:
            return -1
    return k % n + 1

print(solution(food_times, 0, k))


# def solution(food_times, k, x):
#     result = 0
#     for y in range(x, k):
#         if len(food_times) == 0:
#             return -1
#         elif len(food_times) > 0 and food_times[y % n] > 0:
#             food_times[y % n] -= 1
#         else:
#             food_times.pop(y % n)
#             return solution(food_times, k-1-y, y)
#
#     if food_times[(k % n) +1] != 0:
#         result = (k % n) +1
#     return result

