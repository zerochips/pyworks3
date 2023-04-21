# 수학 모듈 - math
# 절대값, 올림, 내림, 제곱근, 원주율, random
import math

# math의 속성
print(math.pi)              # 원주율
print(math.ceil(2.54))      # 정수로 올림
print(math.floor(4.923))    # 내림(버림)
print(math.sqrt(25))        # 제곱근

# 내장 함수
print(round(11.78))

# 절대값
print(abs(-10))


# 절대값을 함수로 정의해보자
"""def my_abs(x):
    if x < 0:
        return - x
    else:
        return x

print(my_abs(-5))   # -5 -> 5, | -5, 5를 넣어도 5가 된다"""

# 절대값 알고리즘 2
def my_abs2(x):
    y = x * x
    return math.sqrt(y)

# 제곱수(양수로 됨) -> 제곱근
print("정수로 나와용~",int(my_abs2(-5)))
# print({int(my_abs2(5)))
print("정수 {}로 나와용~".format(int(my_abs2(5))))











