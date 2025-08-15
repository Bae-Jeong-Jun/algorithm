# 1 <= n <= 15
# t는 기간, p는 금액
n = int(input())

data = [0]*(n+1)
for i in range(1, n+1):
    t, p = map(int, input().split())
    data[i] = [t,p]


def cal(day, payment):
    if day > n:
        return payment

    dt, dp = data[day]
    max_pay = payment

    # 1) 오늘 상담 함
    if day + dt <= n + 1:
        max_pay = max(max_pay, cal(day + dt, payment + dp))

    # 2) 오늘 상담 안 함
    max_pay = max(max_pay, cal(day + 1, payment))

    return max_pay


result = cal(1, 0)
print(result)