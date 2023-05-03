# 계산기 - 간단한 숫자 표시
from tkinter import *

def click1():
    display.insert(END, '1')

def click2():
    display.insert(END, '2')

root = Tk()
root.title("나의 계산기")

# 출력창
display = Text(root, width=30, height=2, bg='orange')
display.grid(row=0, column=0)

# 버튼 생성
Button(root, width=5, text='1', command=click1).grid(row=1, column=0)
Button(root, width=5, text='2', command=click2).grid(row=2, column=0)



root.mainloop()