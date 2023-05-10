# 키워드 매개변수 - **를 사용함
# 딕셔너리 형의 자료로 만들어짐

def print_kw(**kwargs):
    print(kwargs)

# 호출
print_kw(name='진')      # {'name': '진'}
print_kw(age=30, gender='여자')

# ** 별 두개 나오면 딕셔너리구나 하고 생각하면 되겠습니다~

# 가변 매개변수 - * 별 하나
def calc_sum(*numbers):
    sum_v = 0
    for i in numbers:
        sum_v += i
    return sum_v

print(calc_sum(1, 2))
print(calc_sum(1, 2, 6))