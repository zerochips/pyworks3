# Calculator 클래스
class Calculator:
    def __init__(self):
        self.x = 0      # 멤버변수 x에 0을 할당
    
    # 매개변수 y값 더하기
    def add(self, y):
        self.x = self.x + y
        return self.x       # 함수에선 return
    # 매개변수 z값 배기
    def sub(self, z):
        self.x = self.x - z
        return self.x       # 6 = 10 - 4

cal1 = Calculator()
print(cal1.add(10))
print(cal1.sub(4))
print()

cal2 = Calculator()
print(cal2.add(10.1))
print(cal2.sub(2.5))
