# student2 불러와서 사용하기
# 파일을 불러와서 사용하면 두 파일의 정보가 모두 출력되는데
# 원파일에서 메인영역을 설정하면 (if __name__=="__main":)
# 현파일 값만 출력 가능하다

# import 모듈이름
import f_student2                   # 사용법 1
from f_student2 import Student      # 사용법 2
# from 모듈이름 import 클래스이름


# 파일이름.클래스 이름
"""
# st1 = f_student2.Student('이셋', 3) # 사용법 1
st1 = Student('이셋', 3)              # 사용법 2
st1.info()
"""

# 객체 리스트 생성
student = [
    Student("김하나", 1),      #쉼표(,)로 구분
    Student("박둘", 2),
    Student("이셋", 3)
]

# 특정한 학생
#student[0].info()
#student[1].info()
# print(student[0])

print()
# 전체 조회
for i in student:
    print(i)
    #i.info()