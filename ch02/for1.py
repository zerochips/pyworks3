# for ~ in range()
# 1 ~ 10 까지 출력
# range(시작값, 종료값, 증감값)

# 가로로 출력
'''
for i in range(1, 11, 1):
    print(i, end=' ')
print()

# 세로로 출력
for i in range(10, 0, -1):
    print(i)
print()
'''
# 1부터 10까지의 합계
# sum_v = 0 일단 초기화는 해줘야해요
'''
sum_v = 0  
for i in range(1, 11):
    sum_v += i
    print(f'i={i}, sum_v={sum_v}')

print(f'합계 : {sum_v}')
'''

# 1부터 10까지의 홀수 출력
'''
for i in range(1, 11, 1):
    if i % 2 == 1:
        print(i, end = ' ')
print()
for i in range(1, 10, 1):
    if i % 2 == 1:
        print(i, end = ' ')
'''


# print(50 in num)
# print(80 in num)

# 리스트 출력
# print(num)

# 전체 요소를 출력
'''for i in num:
    print(i)'''

# 50보다 큰 수 출력
num = [10, 50, 30, 70]
for i in num:
    if i > 50:
        print(i)

city = ['Seoul', 'Incheon', 'Gwangju']
for i in city:
    print(i[0])

    city = ['Seoul', 'Incheon', 'Gwangju']
for i in city:
    print(i[0], end=' ')
'''
# city[0] : 첫번재 i = Seoul   -> i[0] - 'S'
# city[1] : 두번재 i = Incheon -> i[1] - 'I'
# city[2] : 세번째 i = Gwanju  -> i[2] - 'G'
'''

'''
for i in ['짜장', '짬뽕', '간짜장']:
    print(i)

food = ['짜장', '짬뽕', '간짜장']
for i in food:
    print(i[0])'''
