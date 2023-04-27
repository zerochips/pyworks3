# 재귀 함수
# 종료 조건을 항상 명시(if ~ else 사용하면 된다.)
# 1 부터 10까지 곱하기
# 곱이 for 문 안으로 들어가면 출력값 5 연산오류
"""
def func(입력값):
    if 입력값이 
"""
def getgob(n):
    gob = 1         # 곱셈에서는 1을 기억
    for i in range(1, 6):
        # 곱셈에서는 1을 기억
        gob *= i
        # print(i, gob)          # 결과값 120
        return gob

# getgob()호출
print(getgob(5))

def sos(n):
    print("Help me!!")
    # 종료 조건
    if n == 1:
        return ""
    else:
        return sos(n-1)

sos(3)
# 재귀함수
# 5*4*3*2*1 = 5!(팩토리알, 계승)
# 5*4(5-1)*3(4-1)*2(3-1)*1(2-1) = 5!(팩토리알, 계승)
# 5*4는 5-1과 같죠
def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1)

print(facto(5))
"""
n=5 5* facto(4)
n=4 5* 4* facto(3)
n=3 5* 4* 3* facto(2)
n=2 5* 4* 3* 2* facto(1)
n=1 5* 4* 3* 2* 1
"""
"""
디버깅 해볼게요
n = 3, help me!, sos(2)
n = 2, help me!, help me!, sos(1)
n = 1, help me!, help me!, help me!
"""

"""
def sos(n):
    for i in range(0, n):   # 0은 생략 가능
        print("Help me!")
    # return sos()

sos(3)
"""