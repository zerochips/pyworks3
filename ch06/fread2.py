# season 파일 읽기
try:
    f = open("c:/pyfile/season.txt", 'r')   # 절대 경로

    data = f.read()
    print(data)

    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")