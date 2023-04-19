# 중첩 for 문
# for i in range(5): 5번 반복하라는 거구나 횟수가 중요할 때는 이렇게 써주면 돼요
'''
for i in range(5):  #range(0, 5, 1)
    print(i)
'''
# 세로 출력
'''
for i in range(5):
    for j in range(5):
        print('가')
    print()
'''
# end를 사용해서 5행 5열을 맞췄음
for i in range(5):
    for j in range(5):
        print('가', end=' ')
    print()

# 스타(*) 출력
# 삼각형
"""
*
**
***
****
*****
"""
for i in range(0, 5):
    # * 이 하나씩 늘어남
    for j in range(0, i+1):
        print('*', end=' ')
    print()
    
'''
i=0, j=0                        *
i=1, j=0, j=1                   **
i=2, j=0, j=1, j=2              ***
i=3, j=0, j=1, j=2, j=3         ****
i=4, j=0, j=1, j=2, j=3, j=3    *****
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''

for i in range(0, 5):
    for j in range(1, 6):
        print(5*i+j, end=' ') # 5는 j의 종료값
    print()
print()

row = 5
col = 5

for i in range(0, row):
    for j in range(1, col+1):
        num = col * i + j
        print(num, end=' ') # 5는 j의 종료값
    print()


