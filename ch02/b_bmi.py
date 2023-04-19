# bmi
# 체질량 지수 = 몸무게 / 키(m)의 제곱
# 키 = 키 / 100 -> cm로 환산
# 거듭제곱 2**3 = 2 x 2 x 2
# 거듭제곱 3**2 = 3 x 3
# 과체중이 나오게 만들어 봅시다

name = input('이름을 입력해 주세요: ')
weight = float(input('몸무게를 입력해 주세요: '))   
height = float(input('키를 입력해 주세요: '))
height = height / 100

# 체질량 지수
bmi = weight / (height ** 2)

# 문자일때 %s 라고 해요. 앞은 문자열입니다
# % 퍼센트 포맷 방식 : %s - 문자, %f - 실수, %d - 정수
# .2f 소숫점 2자리까지
print('%s님의 bmi는 %.2f 입니다'% (name, bmi))
# f 스트링(string) 방식일때는 이렇게 써요
# 출력방식이 다양하죠~
print(f'{name}님의 bmi는 {bmi:.2f}')
# 소수점 2자리 까지 설정
print(f'{bmi:.2f}')


if bmi < 20:
    print('저체중 입니다.')
elif bmi >= 20 and bmi < 24:
    print('정상입니다')
elif bmi >= 25 and bmi < 30:
    print('과체중입니다')
else:
    print('비만입니다')

'''
조건 - if
반복 - while, for

if -elif - else
int(문자형 or 실수) -> 정수로 변환
float(문자형) -> 실수로 변환
'''
