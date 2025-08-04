# 테스트 케이스 t
for t in range(int(input())):

    # 1 <= (행의 갯수, 열의 갯수) <= 20
    # m 번에 걸쳐 마지막 열에 도달해야함
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    dp = []

    start = 0
    for _ in range(n):
        dp.append(list(data[start:start + m]))
        start += m

    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 옴
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            # 왼쪽에서 옴
            left = dp[i][j - 1]

            # 왼쪽 아래에서 옴
            if i == n - 1:
                left_under = 0
            else:
                left_under = dp[i + 1][j - 1]
            dp[i][j] += max(left_up, left, left_under)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)