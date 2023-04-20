# 리스트
# a 리스트를 만든거죠
a = [1, 2, 3, 4]

# 리스트에 5를 추가
# insert 하면 중간에 추가할 수도 있어요
# 맨 뒤에서 추가
a.append(5)

# 5를 삭제
#맨 뒤에서 삭제
a.pop()

# a 리스트의 합계와 평균
sum_v = 0

for i in a:
    sum_v += i
avg_v = sum_v / len(a)  # 평균
print(f'[a]합계 : {sum_v}')
print(f'[a]평균 : {avg_v}')

# 내장함수
# print(f'[a]합계 : {sum(a)}')
print(sum(a))

b = (1, 2, 3, 4)    # 괄호를 사용해 볼게요. 이걸 튜플 이라고 하는데
print(sum(b))       # 결과가 print(sum(a)) 랑 똑같이 나와요


print()
# 출력
# 리스트 형식으로 출력이 돼요
# 대괄호로 나오는게 리스트입니다.
print(a)

# 빈 a2에 리스트를 생성해보겠습니다.
# 빈 a2라는 리스트 생성
# a = [1, 2, 3, 4] 위에 있는 a를 가져왔음
'''
a2 = []

a2 = a     # 직접 복사
print(a2)
'''

# for ~ in로 복사
# i가 첫번째 회전할 때 1 두번째 회전할 때 2
'''
a2 = []

for i in a:
    a2.append(i)
print(a2)
'''
# 3의 배수로 복사
a2 = []

for i in a:
    a2.append(3 * i)
print(a2)

# a 리스트에서 홀수만 저장
a3 = []

for i in a:
    if i % 2 == 1:
    # if i % 2 != 0:
        a3.append(i)
print(a3)

# append() 값을 추가하는 함수를 해봤고요









    
