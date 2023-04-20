# 함수 - 입력기능(매개변수를 통해서)
# 사각형의 넓이 계산 함수
# 삼각형의 넓이, 넓이 = (밑변 x 높이) / 2
# 넓이 = 가로의 길이 * 세로의 길이
# 함수이름 - calc_area(), tri_area()
def calc_area(width, height):
    area = width * height
    return area

# 호출
print('사각형의 면적:', calc_area(4, 3))   # 12
print(f'사각형의 면적: {calc_area(4, 3)}')   # 12
# 호출
# 가로 - 4cm, 세로 - 3cm
result = calc_area(4, 3)
print('사각형의 면적:', result)
print(f'사각형의 면적: {result}')
print()
# 삼각형, 밑변 - 4, 높이 - 5
# 나누기가 들어가면 소수가 생겨요
# 잘 확인하세요
def tri_area(s, h):
    area = (s * h) / 2
    return area

print('삼각형의 면적:', int(tri_area(4, 5)))
print(f'삼각형의 면적: {int(tri_area(4,5))}')

result2 = int(tri_area(4, 5))
print("삼각형의 면적:",result2)
print(f'삼각형의 면적: {int(result2)}')


# 정사각형의 면적
'''
size = 4
area = size * size
print(area)

size = int(input("숫자를 입력: "))
area = size * size
print(area)
'''
# 자 이걸 함수로 만드는 겁니다.
'''
def calc_size(n):
    area = n * n
    return area

# print(calc_size(여기에 어떤수를 넣을 수 있는 겁니다. 100을 넣을수도 있고))
print(calc_size(100))
'''















