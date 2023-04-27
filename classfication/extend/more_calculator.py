from classfication.calculator2 import Calculator

# 거듭제곱 계산이 추가된 계산기
class MoreCalculator(Calculator):
    # 2x2x2x2
    def pow(self):
        num = 1
        for i in range(0, self.y):
            num *= self.x
        return num
    
    """
    def pow(self):
        return self.x ** self.y
    """
    """
    def div(self):
        if self.y == 0:
            return 0
        else:
            return self.x / self.y
    """
    def div(self):
        try:
            return self.x / self.y
        except ZeroDivisionError:
            return "0으로 나눌 수 없습니다."

    """
    def div(self):
        try:
            return self.x / self.y
        except ZeroDivisionError as e:
            # return "0으로 나눌 수 없습니다."
            return e
        """

cal = MoreCalculator(2, 4)
print(cal.add(), cal.sub(), cal.mul(), cal.div(), cal.pow())
"""
print(cal.sub())
print(cal.mul())
print(cal.div())
print(cal.pow())
"""
cal2 = MoreCalculator(5, 0)
print(cal2.add(), cal2.sub(), cal2.mul(), cal2.div(), cal2.pow())
"""
print(cal2.sub())
print(cal2.mul())
print(cal2.div())
print(cal2.pow())
"""