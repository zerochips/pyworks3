# 커피 자동판매기 프로그램
# 돈을 일력하면 커피가 나온다.(커피가격: 400)
'''money = int(input("돈을 넣어주세요: "))
price = 400
coffee = 5

if money == price or money >= price:
    print('커피가 나옵니다.'+ (money-price) + )
elif money < price:
    print('커피가 나오지 않습니다.')
else:
    print('커피가 모두 소진되었습니다. 판매를 중지합니다')
'''
coffee = 5

while True:
    try:
        coin = int(input("돈을 넣어주세요: "))
        coffee -= 1

        if coin == 400:
            print("커피가 나옵니다")
            # coffee -= 1
        elif coin > 400:
            print(f"커피가 나오고, 거스름돈{coin-400}원을 돌려 받습니다.")
        else:
            print("커피가 나오지 않습니다.")
        print(f"남은 커피의 양은 {coffee}개 입니다.")

        if coffee == 0:
            print("커피가 모두 소진되었습니다. 판매를 중지합니다.")
            break
    except:
        #print("돈을 넣어 주세요") # 반복됨
        print("다시 결제해주세요.")
        # pass
