import re
str = "123?45yy7890 hi 999 hello"
# \d [0-9]
# \w [a-zA-Z]
# \s []
"""
# compile() - byte 코드로 바꿈
# compile()후 findall() 하면 검색할 내용이 많은 겨우 속도가 빠름
# pet = re.compile('\d{1,3}')   # 숫자 0-9에서 1~3개 까지 찾음(매칭) <- 검색량이 많을땐 이 방법이 빠르다
# m = re.findall(pet, str)

m = re.findall('\d{1,3}', str)
print(m)

m2 = re.findall('[1-5]{1,2}', str)
print(m2)
"""
#################################[ * ]#################################
"""
# '*', '+'의 차이
p = re.compile('ca*t')      # 앞 문자가 0번 이상 반복, 앞 문자가 없어도 됨
m1 = re.findall(p, 'caat')
print(m1)

m2 = re.findall(p, 'ct')
print(m2)                   # 있으면 반복하고 없으면 그대로 출력 - 출력값 : ct
"""
#################################[ + ]#################################
"""
p2 = re.compile('ca+t')     # 앞 문자가 1번 이상 반복 - 없으면 못 찾음
m3 = re.findall(p2, 'caat')
print(m3)

m4 = re.findall(p2, 'ct')
print(m4)                   # 없으면 못 찾음
"""
#################################[ . ]#################################
# 점(.)은 임의의 문자 - 소괄호는 서브클래스(그룹)
str = "abcd<hr>Thank you"
pat1 = re.compile("<(.*)>")     # .*앞에 임의의 문자가 있으면 찾음
m1 = re.findall(pat1, str)      # 소괄호가 <> 안에 있으면
print(m1)                       # <> 없이 hr 만 출력됨

pat2 = re.compile("(<.*>)")     # 소괄호를 <> 밖에 넣으면 <>와 같이 출력
m2 = re.findall(pat2, str)
print(m2)                       # <> 포함해 <hr> 로 출력됨