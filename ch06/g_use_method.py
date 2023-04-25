import g_method1 as met
from g_method1 import get_sum2

# 모듈 이용법
# method1 에 있는 함수를 호출합니다
# import method1 as met인 경우
# get_sum2() 호출
val = met.get_sum2(10)
print(val)

# from g_method1 import get_sum2 을 쓰는 경우 - 이쪽을 더 많이 사용함
val2 = get_sum2(10)
print(val2)

# get_num() 호출
met.get_sum(10)