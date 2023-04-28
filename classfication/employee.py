# 사번 자동 발급
# 보안 - 멤버 변수에 접근하지 않고, 함수를 작성해서 접근
class Employee:
    serial_num = 1000                   # 사번 기줍값(클래스 변수)
    def __init__(self, name):
        # 기줍값을 1증가 한 후 id에 저장함
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name                # 이름은 외부에서 가져오는 값

    def __str__(self):
        return "사번 : {}, 이름 : {}".format(self.id, self.name)

emp1 = Employee("최사원")
# print(emp1.id)                        # 출력값 1001 - print(emp1.id) 보안이 좋지 않음
print(emp1)                             # def __str__(self): return "사번 : {}, 이름 : {}".format(self.id, self.name) 함수를 사용해서 출력 - 보안성 up

emp2 = Employee("유사원")
# print(emp2.id)                        # 출력값 1002
print(emp2)

emp3 = Employee("권사원")
# print(emp3.id)                        # 출력값 1003
print(emp3)

# 객체 리스트로 생성
employee = [
    Employee('구름'),
    Employee('별'),
    Employee('행성'),
    Employee('달')
]

# 전체 출력
for emp in employee:
    print(emp)