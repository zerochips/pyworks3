# 문자열 - 1차원 리스트
'''
ss = '20230419Sunny'
'''
#year = ss[0:4]
# 0없이 적어도 됩니다. 결과값 똑같죠
'''
year = ss[:4]
print(year)
'''
# 월과 일을 day라고 할게요.
'''
day = ss[4:8]
print(day)
'''
# 오늘 날씨 찾아볼게요
'''
weather = ss[8:]
print(weather)
'''
# 합친다
'''
ss2 = year + day + weather
print(ss2)
'''
# 문자열 관련 함수
# split(구분기호) -> 문자열이 리스트로 변환
# 문자열.split()
# 점이 있다는건 객체가 있다는 말이죠
'''
fruit = "banana, apple, strawberry"
'''
# 구분기호가 뭐였죠? 콤마였죠~
'''
fruitlist = fruit.split(',')
print(fruitlist)
print()
'''
# 1번 인덱스 -> apple
'''
print(fruitlist[1])
print()
'''
# replace('이전문자', '새문자')
'''
str1 = 'Hello, World'
str1 = str1.replace('World', 'Korea')
print(str1)
print()
'''
# 문자열.format()

'''
str2 = "My name is {}".format('Mario')
str3 = 'My name is %s.' % 'Mario'
name = "Mario"
str4 = f'My name is {name}'
print(str2)
print()
print(str3)
print()
print(str4)
print()
'''

# 하나 더있죠 하나 더 있을 땐 1을 넣으면 돼요
# 순번이 0번 부터 입니다.
'''
name = "Mario"
year = 40
str2 = "My name is {0}. I am {1}years old.".format('Mario', 40)
print(str2)
'''

# split() 예제 - ':' 기호로 구분하고 리스트로 변경하시오
'''
string = 'a:b:c:d'
print(string)

string2 = string.split(':')
print(string2)
print(string2[-1])
'''
# 두 수를 동시에 입력 받아서 더하기
'''
n1 = int(input("첫번째 수 입력 : "))
n2 = int(input("두번째 수 입력 : "))
'''
# 이제 하나씩 입력하는게 아니고
# 두 수를 동시에 입력하는 방법
# 동시에 받는다
# .split() 공백으로 받는다 .split(':') : 구분한다
'''
n1, n2 = input('두 수 입력 : ').split()

add = int(n1) + int(n2)
print(add)
'''
# find() 함수 - 문자열이 존재하는 위치 반환
text = "Hello"
print(text.find('H'))   # 0
print(text.find('ll'))  # 2
print(text.find('k'))   # -1

print(text.find('Hello'))   # 0

# 회원 정보 출력하기
# 입력
name = input("이름 : ")
user_id = input("아이디 : ")
pw = input("비밀번호: ")
id_card1 = input("주민번호 앞자리 입력: ")
id_card2 = input("주민번호 뒷자리 입력: ")
print('='*30)

# 출력
'''
print("이름 : {}".format(name))
print("아이디 : {}".format(user_id))
pw = '*' * len(pw)
print("비밀번호 : {} ".format(pw))
id_card2 = id_card2[0] + ('*' * 6)
print("주민등록번호 : {0}-{1}:".format(id_card1, id_card2))
'''
print("이름 : {}".format(name))
print("아이디 : {}".format(user_id))
pw = '*' * len(pw)
print("비밀번호 : {} ".format(pw))















