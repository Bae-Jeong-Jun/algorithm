import sys

input = sys.stdin.readline

# 0층 i호에는 i 명 살고 있음
# 밑의 층 1호부터 n호까지 사람 수 합 만큼 살아야함
# k층 n호 거주중인 사람 수 구하기
t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    floor = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, n + 1):
        floor[0][i] = i

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            floor[i][j] = floor[i][j - 1] + floor[i - 1][j]

    print(floor[k][n])












