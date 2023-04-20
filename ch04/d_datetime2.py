# 나이가 100세 되는 해의 연도 계산하기
# 현재년도 + ( 100 - age )
import datetime
import calendar as cal

# print(cal.prcal(2023))
# cal.prcal(2023)
# print(cal.pr<-print를 뜻함 prmonth(2021, 4))
cal.prmonth(2023, 4)


age = int(input("나이를 입력해 주세요 "))
now = datetime.date.today()
print(now.year)

age100 = now.year + (100 - age)
print(f"100세 되는 해는 {age100}년 입니다.")