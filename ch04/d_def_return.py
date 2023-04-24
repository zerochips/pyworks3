# 함수 - return 이 있는 함수
# x 라는 변수에 1을 넣었어요
# 지금 여기는 매개변수 하나 있으니까 
def one_up():       # 1을 더하는 함수
    x = 0           # 지역 변수  
    x = x + 1
    return x

# 이번엔 다르게 해볼게요
def square(x):      # 제곱수를 계산
    val = x * x 
    return val      # 제곱이 되는 겁니다

# 매개변수 두 개 있는거 만들어볼게요
def add(x, y):      # 두 수를 더하는 함수
    val = x + y
    return val

if __name__=="__main__":
    # 함수를 만들었고 호출하고 싶어요
    # print로 바로 출력하는 방법이 있고
    # print(one_up())   # 1
    # print(one_up())   # 1
    print(square(2))

    # 변수를 담아서 호출
    result = square(3)
    print(result)

    # add() 함수 호
    print(add(3,4))
