# 시간 - time 모듈
import time

# 1970. 1. 1 자정 이후 지금 까지 시간을 초로 환산
print(time)
print(time.time())

# round() : 정수로 반올림
# year = round(time.time()/(365*24*60*60), 1) 뒤에 ,1을 사용 하면 실수가 됨
year = round(time.time()/(365*24*60*60))
day = round(time.time()/(24*60*60))
print(year)
print(day)

# 시간에 관련한 모든 정보가 출력됨
# 시간 정보 - 연도, 월, 일, 시, 분, 초
# 이건 로컬 타임이고
print(time.localtime())

# print(time.ctime()) 은 Fri Apr 21 10:12:33 2023 이렇게 출력됨 
# print(time.localtime()) 보다 간결하고 보기 편하게 출력
print(time.ctime())

# 시간 측정
# 종료 시간(time.time()) - 시작 시간(time.time())
# time.sleep(1) - 1초간 대기

# 1부터 100까지
"""for i in range(1, 101):
    print(i, end=" ")

end = time.time()"""

# for i in range(1, 10000001): 출력하는데 걸리는 시간
start = time.time()

for i in range(1, 10000001):
    print(i, end=" ")

end = time.time()
print(f'{end - start: .3f}')
"""
math 모듈이 있어요 - math.ceil(), math.floor()
round는 여기에 빠져있어요 내장함수입니다.
round 자리수가 있으면 실수로가고
자리수가 없으면 정수로 가요
# year = round(time.time()/(365*24*60*60), 1) 뒤에 ,1을 사용 하면 실수가 됨
"""

