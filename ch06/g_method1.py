import time
# 함수 - function, method(메서드)
# 1 ~ 10 까지 출력 for i in range(1, 10+1):
# 1 ~ n 까지 출력 for i in range(1, n+1):
"""
for i in range(1, 11):
    print(i)
"""
# 1 부터 n 까지 출력하는 함수

def get_num(n):
    for i in range(1, 11):
        print(i, end=" ")
get_num(10)     # 호출
print()

# 1부터 n까지 합계를 구하는 함수
# 계산 복잡도 - n번 더하기
"""
start = time.time()
def get_sum(n):
    sum_v = 0
    for i in range(1, n+1):
        sum_v += i
    return sum_v

print(f'합계 : {get_sum(1000000)}')
end = time.time()
print(f'소요시간 : {end-start}초')
"""

# 계산 복잡도 - 곱셈, 덧셉, 나눗셈 - 3번 : 0(1)
start = time.time()                     # time start - 시작하고
def get_sum2(n):
    sum_v = (n * (n+1)) // 2
    return sum_v

if __name__=="__main__":
    print(f'합계 : {get_sum2(1000000)}')
    end = time.time()                       # time end - 맺어주고
    print(f'소요시간 : {end-start}초')