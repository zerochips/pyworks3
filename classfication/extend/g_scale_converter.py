# 단위 변환기 클래스 정의
# 1inch -> 25mm(1*25) 1인치면 (1*25) 2인치면 (2*25)
class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, value):
        return value * self.factor          # 숫자


con = ScaleConverter("inches", "mm", 25)
print("Converting 2 inches")   # 2인치 변환기
print(str(con.convert(2)) + con.units_to)        #str 문자로 변환  # 50mm