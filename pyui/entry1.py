# 이름(문자열)을 입력받고 화면에 출력하기
from tkinter import *

def click():
    text = entry.get()          # 입력상자에 가져온 내용
    output.delete(0.0, END)     # 0-줄번호, 0-시작문자의 위치
    output.insert(END, text)    # text를 출력상자에 삽입
                                # END - 문자열이 입력된 최종 지점까지 삭제후 삽입

root = Tk()
root.title("입력 및 출력")
root.geometry("200x200")

Label(root, text='이름 : ').grid(row=0, column=0)
############################################################
# Entry(root, width=15).grid(row=0, column=1)
# 함수에 사용할 때 나눠줘야함
entry = Entry(root, width=15)
entry.grid(row=0, column=1)
############################################################
btn = Button(root)
btn.config(text='확인', command=click)
# btn.config(command=click)
btn.grid(row=1, columnspan=2)
############################################################
# 가져온 값을 받음
output = Text(root, width=20, height=5)
output.grid(row=2, columnspan=2)
############################################################

root.mainloop()


'''
Button(root)
Label(root)
Entry(root) - 입력상자
text(root) - 출력상자
'''