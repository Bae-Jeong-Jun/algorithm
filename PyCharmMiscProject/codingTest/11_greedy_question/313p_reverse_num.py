data = input()

count0 = 0 #0으로 바꾸는 횟수
count1 = 0 #1으로 바꾸는 횟수

if data[0] == '0':
    count1 +=1
else:
    count0 +=1

# 방법 1
for i in range(1, len(data)):
    if data[i-1] != data[i]:
        if data[i] == '1':
            count0 += 1
        else:
            count1 += 1

# 방법 2
# for i in range(len(data)-1):
#     if data[i] != data[i+1]:
#         if data[i+1] == '1':
#             count0 += 1
#         else:
#             count1 += 1

print(min(count0, count1))