# 산술연산자 - +, -, *, /, %(나머지), //(몫), 거듭제곱(**)
print('10 + 4 =', 10 + 4)
print('10 - 4 =', 10 - 4)
print('10 * 4 =', 10 * 4)
print('10 / 4 =', 10 / 4)
print('10 // 4 =', 10 // 4)
print('10 % 4 =', 10 % 4)
print('10 ** 3 =', 10 ** 3) #10x10x10

# 30개의 빵을 4명이 나눠가질 때 목과 나머지 구하기
# 변수 - bread, people
print()
bread = 30
people = 4

나누기 = int(bread / people)
몫 = bread // people
나머지 = bread % people

print(나누기)
print("빵의 개수:", 몫)
print("남은 빵의 개수:", 나머지)

# 비교연산자
