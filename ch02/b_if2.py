# 다중 조건문 - if ~ elif ~ else
# 놀이공원 입장료 계산
# 8세미만 - 미취학 아동, 14미만 - 초등학생, 20세 미만 - 초, 중등, 20이상 - 일반인
print("♣ 놀이 공원 입장료 계산 ♣")

age = int(input("나이를 입력하세요\n"))
print("당신의 나이는 " + str(age) + "세")

if age < 8:
    print("미취학아동 입니다.")
    charge = 1000
elif age >= 8 and age < 14:
    print("초등학생  입니다.")
    charge = 2000
elif age >=14 and age < 20:
    print("중,고등학생 입니다.")
    charge = 2500
elif age >= 20 and age < 65:
    print("일반인 입니다.")
    charge = str("3,000")
else:
    print("우대시민 입니다")
    charge = 0

# 메인 영역
print("입장료는 " + str(charge) + "원 입니다.")
