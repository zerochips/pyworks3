# 숫자 추측게임
"""
게임 방법
-게임이 시작되면 컴퓨터가 난수(정답)를 생성한다.
-사용자의 추측값이 정담과 같으면 '정답',
-추측값이 정답보다 크면 "너무 커요!",
-추측값이 정답보다 작으면 "너무 작아요!" 출력
"""

import random
"""
# 컴퓨터의 난수 생성
com = random.randint(1, 50)
# print(com)
# min_v = 1
# max_v = 50

num = 0

while True:
    try:
        guess = int(input("맞혀보세요(1~50)> "))

        if num == 10:
            print("기회가 모두 소진되었습니다.")
            break
        else:
            if guess == com:
                print("정답입니다.")
                break
            elif guess > com:
                print("너무 커요!")
                num += 1
                print("기회 " + str(num)+ "회 소진하셨습니다")
                continue
            elif guess < com:
                print("너무 작아요!")
                num += 1
                continue

    except ValueError:
        print("잘못 누르셨습니다.\n다시 눌러주세요")
        continue
"""

com = random.randint(1, 100)
min_v = 1
max_v = 100

try:
    for i in range(0, 10):
        guess = int(input(f"맞혀보세요([{i+1}회]{min_v}~{max_v})> "))

        if guess > 100 or guess < 1:
            print("입력범위가 아닙니다.\n다시 입력해주세요")
        elif guess == com:
            print(f"정답! {com}")
            break
        elif guess > com:
            print("너무 커요")
            max_v = guess
        elif guess < com:
            print("너무 작아")
            min_v = guess
except ValueError:
    print("유효한 숫자가 아닙니다.")

print(f"점수 : {(10-i) * 10}점")

