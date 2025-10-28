# 재귀 함수 사용.
# 깊은 탐색시 RecursionError 발생함

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int,(input()))))

def dfs(i,j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    if data[i][j] == 0:
        data[i][j] = 1 # 방문 처리
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)
        return True
    else:
        return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1

print(count)