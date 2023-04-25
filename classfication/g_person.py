# Person 클래스 정의
class Person:
    def __init__(self, name, age):
        self.name = name        # 생성자(함수)
        self.age = age

    # 멤버의 정보
    def __str__(self):
        return f'이름: {self.name}, 나이: {self.age}'

# 상속 - 자식 클래스이름(부모클래스)
class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id                # 사번 초기화

    # 메서드 재정의(오버라이딩)
    def __str__(self):
        # return f'이름: {self.name}, 나이: {self.age}, 사번: {self.id}'
        # 부모클래스(상위클래스)를 super를 사용해 return값을 받는다
        return f'{super().__str__()}, 사번: {self.id}'

e1 = Employee("이하나", 20, 'a1001')   # a1001 사번 표시
print(e1)


"""
# 클래스 사용 - 객체 생성(메모리 실행)
# p1 - 인스턴스, 오브젝트
p1 = Person("김산", 20)
# print(p1.name)
# print(p1.age)
print(p1)

p2 = Person("이강", 30)
# print(p2.name)
# print(p2.age)
print(p2)
"""