# 파일 쓰기


# 파일 열기(개방) - open(경로, 쓰기모드)
try:
    f = open("c:/pyfile/file1.txt", 'w')

    # 파일 쓰기
    f.write('hello\n')
    f.write('100\n')      # 숫자는 입력할 수 없음 -> 문자형으로 변환
    n = 10 * 2
    f.write(str(n) + '\n')

    for i in range(1, 11):
        text = f'{i}번째 줄입니다.\n'
        f.write(text)

    print("쓰기 완료")
    # 파일 종료
    f.close()
except:
    print("파일 쓰기를 실패 했습니다.")