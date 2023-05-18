# for ~ in range()
# 1 ~ 10 까지 출력
# range(시작값, 종료값, 증감값)
# 가로로 출력
"""
for i in range(1, 11, 1):
    print(i, end=" ")
"""

# 10 ~ 1 까지 출력
"""
for i in range(10, 0, -1):
    print(i)
"""
# 1부터 10까지의 합계
"""
sum = 0

for i in range(1, 11):
    sum += i
print(sum)
"""
# 1부터 10까지의 홀수 출력
"""
for i in range(1, 11):
    if i % 2 == 1:
        print(i, end=" ")
"""
"""
for i in range(1, 10, 1):
    if i % 2 == 1:
        print(i, end = ' ')
"""
# 전체 요소를 출력
"""
for i in num:
    print(i)
"""
# 50보다 큰 수 출력
"""
num = [10, 50, 30, 70]

for i in num:
    if i > 50:
        print(i)

city = ['Seoul', 'Incheon', 'Gwangju']
for i in city:
    print(i[0])
    # print(i)

city = ['Seoul', 'Incheon', 'Gwangju']
for i in city:
    print(i[0], end=' ')

"""
# for ~ in
"""
lang = ['py', 'java', 'C', 'JS']

for l in lang:
    if l in ['py', 'JS']:
        print("인터프리터")
    else:
        print("컴파일러")
"""
# 구구단 출력
"""
dan = int(input("단 수: "))
result = ""

for i in range(1, 10):
    current = f"{dan} x {i} = {dan * i}\n"
    result += current
print(result)
"""
"""
dan = 4
result = ""

for i in range(1, 10):
    current = f"{dan} x {i} = {dan * i}\n"
    result += current
print(result)
"""
# 조건문
# 삼항 연산자 - 조건 연산자 사용안함
# if문의 콜론(:) 코드 블럭을 의미하고 다음줄에서 4칸 들여쓰기(indent-인덴트) 되어야함
# 안됨 왜 안됨?
"""
result = (10 < -10) ? 'T':'F'
print(result)
"""




