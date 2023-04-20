# 교통 수단 이용
# transport
# &&, ||, ! 이런 연산자는 사용안한다고 했죠
# 파이썬 - and, or, not
'''
money = 4000
card = False # 이건 불리언이라고 했죠

if money >= 4000 or card:
    print('택시를 탄다.')
elif money >= 2000 or not card:
    print('버스를 탄다.')
else:
    print('걸어간다.')
'''
'''
pocket = ['paper', '스마트폰', 'money']
print('paper' in pocket)    # True
print('coin' in pocket)     # False
'''
# 리스트를 사용했다 이렇게 이해하면 될 것 같아용~
# 일단 이렇게 하고요 됐죠 여기까지
pocket = ['paper', '스마트폰', 'money']

if 'paper' in pocket:
    print('버스를 탄다.')
else:
    print('걸어간다.')












    
