# 계산기
from tkinter import *
"""
def click(key):
    if key == '=':
        pass
    else:
        display.insert(END, key)
"""

def click(key):
    if key == '=':
        try:                                # eval(문자열 계산) -> 숫자로 변환
            value = eval(display.get())     # 입력된 계산값 eval 계산됨
            result = str(value)[0:10]       # 소수점 포함 10자리까지 출력
            display.insert(END, '=' + result)
        except:
            display.insert(END, "-->오류")   # 예외 처리
    elif key == 'C':                        # 취소 버튼을 누르면 입력값 삭제
        display.delete(0, END)              # 첫번째 문자부터 삭제
    else:
        display.insert(END, key)            # 키값 입력

root = Tk()
root.title("나의 계산기")


# top_row 프레임 - 입력창
top_row = Frame(root)
top_row.grid(row=0, columnspan=2, sticky=N) # N-North(북쪽)
display = Entry(top_row, width=50, bg='orange')
display.grid(row=0, column=0)

##########################[ 숫자 버튼 ]##########################
# num_pad 프레임 - 숫자 버튼
num_pad = Frame(root)
num_pad.grid(row=1, column=0, sticky=W)     # W-West(서쪽)
num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '='
]
r = 0
c = 0
#########[ 중요 ]#########
for btn_text in num_pad_list:
    def cmd(x=btn_text):                    # 함수에 인수(버튼 키)를 전달
        click(x)

    #########[ 숫자 버튼 생성 및 위치 ]#########
    Button(num_pad, width=8, text=btn_text, command=cmd).grid(row=r, column=c)
    c = c + 1
    if c > 2:
        c = 0
        r = r + 1
    # r = r + 1
##########################[ 연산자 프레임 ]##########################
# 연산자 프레임
operator = Frame(root)
operator.grid(row=1, column=1, sticky=E)
operator_list = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C'
]
r = 0
c = 0
#########[ 중요 ]#########
for btn_text in operator_list:
    def cmd(x=btn_text):                    # 함수에 인수(버튼 키)를 전달
        click(x)

    #########[ 연산자 버튼 생성 및 위치 ]#########
    Button(operator, text=btn_text, width=8, command=cmd).grid(row=r, column=c)
    c += 1
    if c > 1:
        c = 0
        r += 1

root.mainloop()