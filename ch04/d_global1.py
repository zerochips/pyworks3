# 지역 변수와 전역변수
"""def one_up():
    x = 0       # 지역변수
    x += 1
    return x"""

"""print(one_up())     # 1
print(one_up())     # 1"""

def one_up2():
    global x   # 전역 변수임을 알려주는 키워드 global을 붙여주면 돼요. 여기 x는 전역변수, 소멸하지 않겠다는
    x += 1
    return x

# 전역변수 # 전역변수는 값을 공유 및 누적 저장,
# 프로그램 종료시 메모리에서 소멸

x = 0
print(one_up2())    # 1
print(one_up2())    # 2
print(one_up2())    # 3
print(x)  # 마지막 값과 동일하다