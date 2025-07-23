n = int(input()) # 학생 수

students=[]

for _ in range(n):
    students.append(input().split())

# 튜플 원소로 하는 리스트를 정렬
students.sort(key = lambda x : (-int(x[1]), (int(x[2])), (-int(x[3])), x[0]))

for student in students:
    print(student[0])






