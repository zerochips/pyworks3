# pickle 모듈 사용
# pickle 모듈 - 객체의 형태를 그대로 유지하면서 파일을 읽고 쓰는 모듈
# 객체(리스트, 딕셔너리) 형태를 그대로 유지하여 저장하고 읽어옴
# pickle.dump - 쓰기, pickle.load - 읽기
# 추가 'a'
import pickle

with open("./output/object.txt", "wb") as f:
    a = ['강아지', '고양이', '말']
    dic = {1:'강아지', 2:'고양이', 3:'말'}
    pickle.dump(a, f)   # 쓰기
    pickle.dump(dic, f)

with open("./output/object.txt", "rb") as f:
    a = pickle.load(f)
    dic = pickle.load(f)

    print(a)
    print(dic)

