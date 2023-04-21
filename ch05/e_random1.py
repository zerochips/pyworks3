# random 모듈
# 숫자(정수)를 랜덤 추출 - 1 ~ 10 : random.randint(1, 10)
# 리스트에서 요소 추출 - random.choice(리스트)

import random
# 1 부터 10 중 무작위로 추출 하는 방식
'''
num = random.randint(1, 10)
print(num)

# 주사위 만들기
dice = random.randint(1, 6)
print(dice)

# 주사위 10번 던지기
for i in range(0, 10): # 0~9
    dice = random.randint(1, 6)
    print(dice, end=" ")

# 리스트에서 랜덤하게 값을 추출하기
과일 = ['딸기', '수박', '참외', '사과']
# print(과일[0])
# print(과일[-1])
print(random.choice(과일))
'''
# 지역 = ['서울', '부산', '경기', '인천']

# 주사위 2개를 10번 던지기
# 두 눈의 합이 7이면 "Seven Thrown!!" 출력, 11이면 "Eleven Thrown"
# 두 눈의 수가 같으면 "Double Thrown!!" 출력
for i in range(10):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print(total)
    if total == 7:
        print("Seven Thrown!!")
    if total == 11:
        print("Eleven Thrown")
    if dice1 == dice2:
        print("Double Thrown!!")
