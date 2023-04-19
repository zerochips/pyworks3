# 자료구조 - 딕셔너리(dictionary)
# person 이라는 자료구조를 만든다 그 안에 속성이 있잖아요
# 이름 이라던지
# {key: value}
# 똑같은 형식으로 나와요
# 리스트는 순서가 있는반면
# 여긴 순서가 없어요. 인덱싱은 하지 않음
person = {'name':'오상식', 'age':35, 'phone':'010-1234-5678'}
# print(person)

# 특정 요소 출력
'''
print("이름:", person['name'])
'''
# 전체 출력
'''
for key in person:
    # print(키, 값)
    print(key, ':', person[key])
'''

# 요소 추가
# []여기다가 항목을 넣으면 돼요
# 맨 뒤에 들어가요
# list는 뭐였죠? append 썼었죠?
# 출력하면 안나오죠~ 위 for문을 아래로 내리면 나올겁니다.
person['email'] = 'green@green.com'
'''
for key in person:
    # print(키, 값)
    print(key, ':', person[key])
'''

# 요소 삭제
# 내가 만약에 폰을 삭제하고 싶다.
# 삭제 방법 1
# del person['phone']

# 삭제 방법 2
# 지정한 key값으로 삭제
# 순서가 없으니가 맨 뒤가 없죠
# 그래서 키값을 넣는겁니다.
person.pop('phone')

# 요소 수정
# 나이를 30으로 바꿔볼게요
person['age'] = 30

# 전체 출력
'''
for key in person:
    # print(키, 값)
    print(key, ':', person[key])
'''

# 용어 사전
print('♠ 용어 사전 ♠')
# 다운되면 어떻게 해줘야된다고 했죠?
# try: except: 를 사용하면 된다고 했죠
# 없는거 입력하면 틀리죠
# tab을 사용하거나 4칸이 들어가야 실행이 됩니다.
# 아니면 오류나요
'''
try:
    word = input('단어를 입력하세요: ')

# 이게 자료구조죠 
    dic = {
        "이진수" : "컴퓨터가 사용하는 0과 1로 이루어진 수",
        "버그" : "프로그램이 적절하게 동작하는 데 실패하거나 오류가 발생하는 코드",
        "알고리즘" : "어떤 문제를 해결하기 위해 정해진 일련의 절차"
    }

# print(dic['이진수'])
# except: 는 제일 마지막에 들어가야 실행이 돼죠

    definition = dic[word]
    print(definition)
except:
    print("정의된 단어가 없습니다.")
'''
# 작업하다가 Error가 나~ 그때 keyError가 났었어요
# try ~ except 할 때 넣어주는 겁니다. except KeyError: 
# KeyError: 를 넣어도 되고 안넣어도 된다는 겁니다.

while True:
    word = input("단어를 입력하세요")

    if word:
        print("반복합니다")
    elif word == '중단' or word == '중지' or word == '그만' or word == '멈춰':
        print("반복을 중단합니다.")
        break
    else:
        print("ㅇ")






