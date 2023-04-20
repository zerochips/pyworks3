# 주석
# 자료형 - 숫자, 문자, 불리언, 리스트, 객체
# 여러줄 주석 : """ 쌍따옴표(홀따옴표) 3개를 쌍으로 적음.
'''
print(12)
print(type(12)) #type()함수 <int - integer(정수형)>

print(3.3)
print(type(3.3)) # <float - 실수형>
'''
n = 1 #변수 선언 방법 - 자료형은 생략
print('n =', n, '개') #콤머(,)는 한 칸 띄움
print('n = ' + str(n) + '개') #str(숫자) - 문자로 변환함

msg = "좋은 하루!!"
print('메시지 :', msg)
#print(type(msg)) # <class 'str'>

num = int('120') #int(문자형) - 정수로 변환함
print(num)

num2 = int(120.7) # 120 실수
print(num2)

# 불리언(참/거짓)
state = True
print(state)  #True - 첫글자 대문
print(not state) #False

print(10 > 11) #False
print(10 < 11) #True








'''
DB 모델링 툴
- Lucid Chart
- EX ERD : 자바 이클립스 연동
- ER win : 유료, 쉐어웨어(사용)


파이썬 쉘
- python 명령어를 적으면 쉘 상태임
- 입출력(print함수 생략) 할 수 있음
- 저장이 안됨 -> Editor(IDE)
- 종료(quit() 함수, ctrl + z)

자료형 키워드(var, int) 없음
'''
