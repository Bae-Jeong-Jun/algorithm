n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = triangle[i-1][j-1]
        if i == j:
            up_right = 0
        else:
            up_right = triangle[i-1][j]
        triangle[i][j] = triangle[i][j] + max(up_left, up_right)

print(max(triangle[n-1]))