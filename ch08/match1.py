# match(), search() 객체의 메서드
# 그루핑(grouping())
import re

# 패턴을 통해서 매치시키는건데
# 매치는 시작위치부터 찾는다
"""
p = re.compile('[a-z]+')
m = p.match('hello')

print(m.group())    # 문자열 출력
print(m.start())    # 시작 인덱스 - 0
print(m.end())      # 끝 인덱스 - 5->(5-1)
print(m.span())     # 구간(시작, 끝)
"""

# 이름과 전화번호를 분리해서 추출하기

str = "lee 010-1234-5678"
"""
# 정규표현식은 컴파일에 씁니다.
# pat = re.compile("\w+")
# \s <- 공백하나만 적용됨 | \s <- 여러 공백가능
# () 소괄호가 그룹
# pat = re.compile("\w+\s{1,2}\d")                  # 공백이 1개나 2개
# pat = re.compile("\w+\s{1,2}\d+[-]")              #
# pat = re.compile("(\w+)\s{1,2}\d+[-]\d{4}[-]\d{4}") #
pat = re.compile("(\w+)\s{1,2}(\d+[-]\d{4}[-]\d{4})") #
mat = pat.match(str)
print(mat)
print(mat.group())
print('이름:', mat.group(1))
print('전화번호:', mat.group(2))
"""

# 그룹핑된 문자열에 이름 붙이기
# 정규 표현식 - (?P<그룹이름>)
pat2 = re.compile('(?P<name>\w+)\s{1,2}(?P<phone>\d+[-]\d{4}[-]\d{4})')
mat2 = pat2.match(str)
print('이름:', mat2.group('name'))
print('전화번호:', mat2.group('phone'))

# sub(\g<그룹이름>)
s1 = pat2.sub('\g<name>', 'park 010-3333-4444')
s2 = pat2.sub('\g<phone>', 'park 010-3333-4444')
print('이름:', s1)   # 객체를 출력하는
print('전화번호:', s2)   # 객체를 출력하는

# 문자열 바꾸기
# 뒤를 마스크 처리를 하고 싶어~ 1234567
data = """
kim 871212-1234567
lee 770707-2345678
"""
# 소괄호가 있는 상태로 만들어줘야 되죠
# jumin = re.compile("(\d+)[-]\d+")
jumin = re.compile("(\d+)[-]\d+")
jumin = jumin.sub('\g<1>-*******', data)
print(jumin)

# 전화번호 맨 끝자리 **** (마스크 처리)
data = """
park 010-1234-5678
han 010-4567-8901
"""

ph = re.compile("(\d{2,3})[-](\d{3,4})[-](\d{3,4})")
ph = ph.sub('\g<1>-\g<2>-****', data)
print(ph)