class City:
    a = ['Seoul', 'Incheon', 'Daejon', 'Jeju']      # 클래스 리스트

str1 = ""
for i in City.a:                    # 클래스 이름으로 직접 접근
    str1 += i                       # c = City()
                                    # print(c.a) 이런 방법으로 접근할 수 있겠지만 이렇게 사용하지 않음 (9-10 line)

print(str1)

"""
    def __init__(self, name):       # 얘는 따지고 보면 인스턴스 변수라고 했잖아요 4, 5 line
        self.name = name
        self.a2 = []                # 인스턴스 리스트
"""