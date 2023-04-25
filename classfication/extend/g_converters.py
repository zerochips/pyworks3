# ScaleConverter 상속받는 클래스
# 모듈(파일)은 import해서 사용해야하죠
# import 패키지이름.모듈이름
# import 패키지이름.모듈이름 import 클래스
# import classfication.g_scale_converter
#from classfication.g_scale_converter import ScaleConverter
from classfication.extend.g_scale_converter import ScaleConverter    # 폴더안의 모듈을 불러올 땐 폴더명을 앞에 쓰고 연결문자 . point를 붙인 뒤 똑같이 연결시켜줌

con = ScaleConverter("KB", "B", 1024)
print("Converting 1 KB")
print(str(con.convert(1)) + con.units_to)

# 화씨온도(F) = 섭씨온도(C) x 1.8 + 32

class Converter(ScaleConverter):
    def __init__(self,units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor)  # 부모 멤버 상속받음
        self.offset = offset

    def convert(self, value):
        # return self.factor * value + self.offset
        return super().convert(value) + self.offset

conv = Converter('C', 'F', 1.8, 32)
print("Converting 20c")
print(f'{conv.convert(20):.2f}{conv.units_to}')