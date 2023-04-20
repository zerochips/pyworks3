# 날짜 및 시간 모듈 포함하기
import datetime

# print(datetime.datetime.today())
now = datetime.datetime.today()
print(now)
# now는 객체잖아요
print(now.strftime("%Y.%M.%D. %H:%M:%S"))
print()
# 날짜 - 년, 월, 일
print(f'{now.year}년 ')
print(f'{now.month}월 ')
print(f'{now.day}일 ')
print()
# 시간 - 시, 분, 초
print(f'{now.hour}시 ')
print(f'{now.minute}분 ')
print(f'{now.second}초 ')

# 오늘의 날짜
# 날짜만 필요하다~
today = datetime.date.today()
print(today)

# 특정한 날짜
the_day = datetime.date(2024, 12, 12)
print(the_day)