# 백신 접종자 분류
# int를 처음에 하면
'''
birth = input("출생년도 입력 : ")
age = 2023 - int(birth) + 1

if age >=20 and age < 65:
    print("백신 접종 대상")
    # 접종대상 : 출생년도 끝자리 비교
    # if ~ elif ~ else
    print(birth)
    if birth[-1] == '1' or birth[-1] == '6':
        print("월요일 접종")
    elif birth[-1] == '2' or birth[-1] == '7':
        print("화요일 접종")
    elif birth[-1] == '3' or birth[-1] == '8':
        print("수요일 접종")
    elif birth[-1] == '4' or birth[-1] == '9':
        print("목요일 접종")
    else:
        print("금요일 접종")    
else:
    print("하반기 일정 확인")
'''

birth = int(input("출생년도 입력 : "))
year = 2023
age = year - birth + 1

if age >=20 and age < 65:
    print("백신 접종 대상")
    birth = str(birth) # 문자열로 변환
    if birth[-1] == '1' or birth[-1] == '6':
        print("월요일 접종")
    elif birth[-1] == '2' or birth[-1] == '7':
        print("화요일 접종")
    elif birth[-1] == '3' or birth[-1] == '8':
        print("수요일 접종")
    elif birth[-1] == '4' or birth[-1] == '9':
        print("목요일 접종")
    else:
        print("금요일 접종")    
else:
    print("하반기 일정 확인")
