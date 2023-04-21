# turtle 모듈
import turtle as t

t.shape("turtle")

"""
# forward(픽셀크기) - 직진
t.forward(100)      #직진 100px
t.left(90)          # 머리 방향이 왼쪽으로 90도
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
"""

"""
for i in range(0, 4):
    t.left(90)
    t.forward(100)
"""

# 삼각형을 그리며 이동
"""
t.bgcolor('orange')
t.color('blue')
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
"""
for i in range(0, 4):
    t.right(90)
    t.forward(100)

t.color('blue')
t.shapesize(5)      # 거북이 사이즈 키우기
for i in range(0, 3):
    t.left(120)
    t.forward(100)

t.color('red')
t.pensize(3)
t.circle(50) # 반지름이 50px인 원



t.mainloop()

"""메이플 만든 사람이 만들었음 대박"""