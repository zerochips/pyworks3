# 함수 - 매개변수 리스트
# 리스트의 합계, 최대값, 최소값

# 리스트의 합계 연산하는 함수 정의 - get_sum()
# 매개변수 - 리스트
def get_sum(a):
    sum_v = 0   # sum_v 초기화를 해줘야 합니다
    for i in a:
        sum_v += i
    return sum_v   # return 반환하는 - 보내주는거죠

# 리스트의 평균을 계산하는 함수
def get_avg(a):
    sum_v = 0
    for i in a:
        sum_v += i
    return sum_v / len(a)

# 리스트의 최대값을 구하는 함수
def get_max(a):
    max_v = a[0]            # 리스트의 첫번째 값을 최대값으로 설정
    for i in v:
        if max_v < i:
            max_v = i
    return max_v

def get_min(a):
    min_v = a[0]            # 리스트의 첫번째 값을 최대값으로 설정
    for i in v:
        if min_v > i:
            min_v = i
    return min_v

'''
min_v = 3  i = 3, 3 > 3  False
           i = 2, 3 > 2  True
           i = 5, 2 > 5  False
           i = 1, 2 > 1  True
           i = 4, 1 > 4  False
'''
v = [3, 2, 5, 1, 4]
print("합계 : ", get_sum(v))
print("평균 : ", get_avg(v))
print("최대값 : ", get_max(v))
print("최소값 : ", get_min(v))

"""
# 기본적인 상태
v = [1, 2, 3, 4]
sum_v = 0       # 합계 sum_v 라는 변수에 담아야하죠

for i in v:
    sum_v += i

# 출력
print(sum_v)
"""

# print(sum(v))
# print(max(v))
# print(min(v))

# 최대값
"""
v = [1, 3, 9, 7, 5]
max_v = v[0]

# 연산
for i in v:
    if max_v < i:
        max_v = i

# 출력
print(max_v)
"""
