# 매개변수가 리스트로 함수
# v = [1, 2, 3, 4] 리스트 복사를 함수를 이용해서 해볼게요
# def 함수
# v라는 변수는 a와 같다.
'''
def get_list(a):
    a2 = []
    for i in a:
        a2.append(i)
    return a2
'''
def get_list(a):
    a2 = []
    for i in a:
        a2.append(2 * i) # 2의 배수로 표현하면
    return a2

v = [1, 2, 3, 4, 5]
# get_list에 v를 담아서 호출해요
# 자료를 대량을 넘겨야할 때는 이렇게 해야 하니까
print(get_list(v))  # [1, 2, 3, 4]
