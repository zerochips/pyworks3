# 키보드로 거북이 조종하기
import turtle as t

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def clear():
    t.clear()   # 화면 지우기

t.shape('turtle')
t.color('orange')
# 함수 호출시 괄호가 없음 - 주의!, Right - 첫글자 대문자(상수)
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(clear, 'Escape')

t.listen()    # 키가 작동하는 걸 대기중

t.mainloop()

# 오른쪽 화살표 눌렀을 때
# t.setheading(0) -> 오른쪽
# t.setheading(90) -> 위
# t.setheading(180) -> 왼쪽
# t.setheading(360) -> 아래