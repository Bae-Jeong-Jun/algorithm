# 0은 홈 부분, 1은 돌기 부분
# 열쇠의 돌기 부분과 자물쇠의 홈 부분이 일치해야 함

# key 시계 방향으로 회전
def rotate_a_matrix_by_90_degree(a):
    m = len(a)  # 행
    n = len(a[0])  # 열
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

# new_lock의 중앙부가 모두 1인지 확인
def check(new_lock):
    n = len(new_lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    # lock 크기의 3배인 new_lock 생성
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    # 열쇠 회전
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n * 2):
            for y in range(n * 2):
                # 열쇠 삽입
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                # False 시 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    # new_lock에 열쇠 삽입 못할시
    return False

# key는 M x M lock은 N x N
# M <= N
m, n = map(int, input().split())
key = [list(map(int, input().split())) for _ in range(m)]
lock = [list(map(int, input().split())) for _ in range(n)]

print(solution(key, lock))












