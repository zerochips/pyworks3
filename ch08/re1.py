# re모듈을 임포트함
import re

# / 정규표현식 /g -> re.compile("정규표현식")
# 소문자 a부터 z까지 일치하는 문자를 반복해서 찾음
# match() - 일치하는 문자를 찾는 함수
p = re.compile("[a-z]+")

m1 = p.match('afternoon')       # 처음 부터 일치해야 찾음
print(m1)           # m1 객체
print(m1.group())   # 문자열 출력

m2 = p.match('2023 good luck')  # 숫자가 있어서 현 정규표현식 조건으론 못 찾음
print(m2)

s1 = p.search('2023 good luck') # 전체 중 일치하는 조건 찾음 - good 만 출력됨
print(s1)
print(s1.group())