# m의 크기가 클때
n, m ,k = map(int, input().split())
data = list(map(int,input().split()))
data = data[:n]
data = sorted(data, reverse=True)

first_count = (m//(k+1)*k + m%(k+1))
second_count = m - first_count
result = 0
result += data[0]*first_count
result += data[1]*second_count

print(result)