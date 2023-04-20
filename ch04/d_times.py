# 배수를 구하는 함수를 정의하고 사용
# 배수의 개수 구하기

"""def times(x):
    global count
    for i in range(1, 31):
        if i % x == 0:
            count += 1
            print(i, end=' ')

count = 0
times(3)

print()
print("배수의 개수 : %d" % count)"""

# 배수의 개수를 한다고하면 for문을 먼저 작성해야 합니다.
# 1부터 31까지라고 했으니까 

"""
# 첫번째
for i in range(1, 31):
    if i % 3 == 0:      # 위에는 i로 표시 3은 현재는 3의 배수
        count += 1
        print(i, end=' ')"""

"""# 두번째
def times(x):
    for i in range(1, 31):
        if i % x == 0:
            print(i, end=' ')

times(3)"""

# 세번째
"""def times(x):
    global count
    for i in range(1, 31):
        if i % x == 0:
            count += 1
            print(i, end=' ')
    print()
    print(count)

count = 0
times(3)
print(f'\n배수의 개수 : {count}')
"""

def times(x):
    global count
    for i in range(1, 31):
        if i % x == 0:
            count += 1
            print(i, end=' ')

count = 0
times(3)

print()
print("배수의 개수 : %d" % count)