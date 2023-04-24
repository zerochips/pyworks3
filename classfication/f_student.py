# 객체 지향 언어 - 모든 사물을 객체화(Object)
# 객체화를 위해 코드로 정의한 것 - class
class Student:
    # 멤버 변수
    name = ""   # 자료형 문자
    grade = 0   # 자료형 숫자

    def info(self):     # self를 붙여야 함
        print(self.name, self.grade)
        


# 객체로 만드는 방법
std1 = Student()    # 객체 생성(인스턴스)
std1.name = '김하나'
std1.grade = 1
# print(std1.name, std1.grade)
std1.info()

std2 = Student()
std2.name = '박둘'
std2.grade = 2
# print(std2.name, std2.grade)
std2.info()








"""
자바 - 클래스(순수 객체 지향)
객체 지향 언어의 특성 - 추상화, 캡슐화, 상속, 다형성

class 클래스A:
       변수
       함수(def)

상속
class 클래스이름(A):
       변수
       함수(def)

classfication(분류)
"""
