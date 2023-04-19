# 점수 통계 같은걸 해볼까요?
# 성적 처리
# 학생 5명의 국어 점수  - 합계, 평균, 최고점수, 최저점수
A = [70, 80, 50, 60, 90]
'''
for i in A:
    print(i)
'''
# 1 ~ 5까지 출력할 때 어떻게하죠
# for i in range(1, 6, 1): 쓰는데for i in range(1, 6): 이렇게 생략하자고 그랬죠
'''
for i in range(1, 6, 1):
    print(i)
'''

# for~in range() - 인덱스 방식
'''
for i in range(0, len(A)):
    print(A[i], end=' ')
''' 
# for~ in 방식이 있고 for ~ in range() 방식이 있어요 약간 달라요
# 이거 어떻게 하냐
# 시작값이 i겠죠 종료값은 
# for i in range(i, ):

# 옆으로 찍고 싶을 때는 end=' ' 이렇게 사용하라고 했죠
'''
for i in A:
    print(i, end=' ')
'''
# 합계 구하려면 개수를 구해야죠
# count 어떤 함수가 있었죠 len

count = len(A)

# print(count)

# 합계
sum_v = 0

for i in A:
    sum_v += i # 0 + 70이야
    print(f'i={i}, sum_v={sum_v}')
print('합계:', sum_v)

# 평균
avg = sum_v / count
# 소숫점 첫번째자리까지 나오게 하려면 .1f 하면 되겠죠
print(f'평균: {avg:.1f}')

# 최고점수 구해볼까요
# 내장함수 - sum(), max(), min()
# 여러분들 나중에 이렇게 쓰면 돼요
# 그런데 우리는 기초를 알아야 하니까 그래요
# 내장함수에 빌트인 함수로 지원되고 있어요
print(sum(A))
print(max(A))

































