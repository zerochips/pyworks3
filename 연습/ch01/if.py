# 자동차 주행속도가 50km 이상이면 "안전 속도 위반!! 10만원 부과대상"
# 50km 미만이면 "안전 속도 준수"를 출력하는 프로그램
"""
speed = 51

if speed >= 50:
    print("안전 속도 위반!! 10반원 부과 대상")
else:
    print("안전 운행")
print("현재 속도는 " + str(speed) + "km 입니다.")
"""
# 다중 조건문 - if ~ elif ~ else
# 놀이공원 입장료 계산
# 8세미만 - 미취학 아동, 14미만 - 초등학생, 20세 미만 - 초, 중등, 20이상 - 일반인
"""
print("♣ 놀이 공원 입장료 계산 ♣")
try:
    age = int(input("나이를 입력해 주세요: "))

    if age < 8:
        price = 1000
        print("미취학 아동입니다.")
    elif age >= 8 and age < 14:
        price = 2000
        print("초등학생입니다.")
    elif age >= 14 and age < 20:
        price = 2500
        print("청소년입니다.")
    elif age >=20 and age < 65:
        price = 300000000
        print("일반인 입니다.")
    else:
        price = 0
        print("우대시민 입니다.")
    print(f"입장료는 {price:,}원 입니다.")
except ValueError:
    print("잘못 입력하셨습니다.\n다시 입력해주세요.")

"""

print("♣ 놀이 공원 입장료 계산 ♣")

def money(age):
    if age < 8:
        return 1000
    elif age >= 8 and age < 14:
        return 2000
    elif age >= 14 and age < 20:
        return 2500
    elif age >= 20 and age < 65:
        return 300000000000
    else:
        return 0

try:
    age = int(input("나이를 입력해 주세요: "))

    price = money(age)
    print("입장료는 {:,}원 입니다.".format(price))
except ValueError:
    print("잘못 입력하셨습니다.\n다시 입력해주세요.")