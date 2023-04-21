# 지나온 날짜 계산하기 : 일수 = 종료일 - 시작일
# datetime.date(종료일) - datetime.date(시작일)
# 요일은 뭐였죠 요일 같은 경우
# 요일(인덱스) - datetime.date(특정일).weekday(), 월-0번
import datetime
import calendar

day1 = datetime.date(2023, 3, 16)
print(day1)
print(" ♠ 지금 까지 몇 일? ♠ ")
# today = datetime.date(2023, 4, 21)
today = datetime.date.today()
print(today)

passed_time = today - day1
# print(passed_time)
# print(passed_time.days,'Day')
# 날짜객체.days ->일(day)로 환산
# f 스트링 방식 말고 포멧 방식을 사용해서 프린트 해볼게요
print("개강 이후 {}일이 지났습니다.".format(passed_time.days))
# print("000{}000".format(000.days))

# 날짜로 요일 알아내기
days = ['월', '화', '수', '목', '금', '토', '일']

# datetime.date(2023, 3, 16).weekday()
# 3 출력, 인덱스 3번은 목요일
the_day = datetime.date(2023, 3, 16).weekday()
print(the_day)
# print(days[the_day]+ "요일")
print(f'{days[the_day]}요일')

# now = datetime.date.today().weekday()
now = datetime.date.today().weekday()
print(f'{days[now]}요일')

# 2023년 전체 출력
calendar.prcal(2023)

# 2023년 3월 출력
calendar.prmonth(2023, 3)

"""함수
모듈 - 파일(datetime.py, random.py) 파이썬에선 모듈이 파일입니다.
파이썬은 밀리초가 아니고 ms -> 초(s)단위 입니다
클래스
"""