# 학생의 4명 성적 통계
# 한 사람일 때의 방법
# student = {'name':'이대한', 'kor':80}

# 한 명 이상일 때
# 갑자기 리스트가 됐어요
student = [
    {'name': '이대한', 'kor': 80, 'eng': 80, 'math': 75},
    {'name': '박민국', 'kor': 70, 'eng': 65, 'math': 60},
    {'name': '오상식', 'kor': 75, 'eng': 70, 'math': 50},
    {'name': '최지능', 'kor': 70, 'eng': 90, 'math': 90},
]
# print(len(student))
# std 가 한 번 회전할 때 {'name':'이대한', 'kor':80, 'eng':80, 'math':75} 이게 나와요
# 두번 회전할 때 {'name':'박민국', 'kor':70, 'eng':65, 'math':60} 이게 나오는거죠
# print(std['name']) 출력을 이렇게하면 이름만 나오는거죠
# print(student[0])
# print(len(student))

print('== 개인별 성적표 ==')
print('이름   국어 영어 수학')
for std in student:
    # print(std['name'], std['kor'], std['eng'], std['math'])
    print(f"{std['name']}  {std['kor']}  {std['eng']}  {std['math']}")
print()

# 개인별 총점
# 구해볼게요
print('== 개인별 총점 ==')
print('이름   총점  평균')
for std in student:
    total = std['kor'] + std['eng'] + std['math']
    avg = total / 3
    print(f"{std['name']} {total} {avg:0.2f}")

# 과목별 총점과 평균
sum_subj = [0, 0, 0]  # [국어총점, 영어총점, 수학총점]
avg_subj = [0, 0, 0]
for std in student:
    sum_subj[0] += std['kor']
    sum_subj[1] += std['eng']
    sum_subj[2] += std['math']
print()

print("== 과목별 총점 ==")
print('국어 영어 수학')
print(f"{sum_subj[0]} {sum_subj[1]}  {sum_subj[2]}")
# print(f"국어 총점 : {sum_subj[0]}\n영어 총점 : {sum_subj[1]}\n수학 총점 : {sum_subj[2]}\n")
# print(f"국어 총점 : {sum_subj[0]}")
# print(f"영어 총점 : {sum_subj[1]}")
# print(f"수학 총점 : {sum_subj[2]}")
print()
# 과목별 평균
avg_subj[0] = sum_subj[0] / len(student)
avg_subj[1] = sum_subj[1] / len(student)
avg_subj[2] = sum_subj[2] / len(student)

print("== 과목별 평균 ==")
print('국어    영어  수학')
print(f"{avg_subj[0]} {avg_subj[1]} {avg_subj[2]}")
# print(f"국어 평균 : {avg_subj[0]}")
# print(f"영어 평균 : {avg_subj[1]}")
# print(f"수학 평균 : {avg_subj[2]}")