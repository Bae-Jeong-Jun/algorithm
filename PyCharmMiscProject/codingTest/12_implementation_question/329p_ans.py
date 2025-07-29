# 보통의 알고리즘 문제는 1초에 1억번 연산 가능
# 2차원 벽면 nXn. n <= 5 < =100
# m : 설치,삭제 총 횟수
n,m = map(int, input().split())

# build_frame [x,y,a,b]
# a : 0 = 기둥, 1 = 보
# b : 0 = 삭제, 1 = 설치
build_frame = [list(map(int, input().split())) for _ in range(m)]

def check(result):
    for dx,dy,da in result:
        # 기둥 확인
        if da == 0:
            if dy == 0 or [dx, dy-1, 0] in result or [dx-1, dy, 1] in result or [dx, dy, 1] in result:
                continue
            return False
        # 보 확인
        if da == 1:
            if [dx, dy-1, 0] in result or [dx+1, dy-1, 0] in result or ([dx-1, dy, 1] in result and [dx+1, dy, 1] in result):
                continue
            return False
    return True

result = []
for x, y, a, b in build_frame:
    # 설치
    if b == 1:
        result.append([x,y,a])
        if not check(result):
            result.remove([x,y,a])
    # 삭제
    elif b == 0:
        result.remove([x,y,a])
        if not check(result):
            result.append([x, y, a])

print(sorted(result, key = lambda x: (x[0], x[1], x[2])))
















