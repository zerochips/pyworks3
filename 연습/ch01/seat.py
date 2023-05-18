# 자리배치
# 입장객 수, 좌석 열, 줄수
# 입장객수가 열수로 나눠어떨어지는 경우, 그렇지 않은 경우
while True:
    try:
        입장객 = int(input("입장객 수 입력: "))
        좌석열수 = int(input("좌석 열 수 입력: "))
    
        if 입장객 % 좌석열수 == 0:
            줄 = int(입장객 / 좌석열수)
        else:
            줄 = int(입장객 / 좌석열수) + 1
    
        for i in range(줄):
            for j in range(1, 좌석열수 + 1):
                seat = 좌석열수 * i + j
                if seat > 입장객:
                    break
                print("seat", seat, end=" ")
            print()
    except ValueError:
        print("잘못 입력하셨습니다.\n다시 입력해주세요")

    answer = input("다시 하시겠습니까?(y/n) ")
    if answer == 'n' or answer == 'N':
        print("프로그램을 종료합니다.")
        break
    elif answer != 'y' or answer != 'Y':
        print("잘못 입력하셨습니다.")
        continue


"""
print("줄수", row)

if row > customer:
    print(customer)
    """