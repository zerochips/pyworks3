# 다각형 그리기
import turtle as t

t.shape('turtle')

def polygon(n):             # 매개변수 - 도형의 변의 개수
    for i in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n, d):
    for i in range(n):
        t.forward(d)
        t.left(360/n)

polygon(3)
polygon(5)

t.up()      # 펜 올리기
t.forward(100)
t.down()    # 펜 내리기

polygon2(3, 100)
polygon2(5, 100)

"""
t.speed(5)

for i in range(3):
    t.forward(100)
    t.left(120)

t.up()
t.right(90)
t.forward(150)
t.down()

for i in range(3):
    t.forward(100)
    t.left(120)

for i in range(4):
    t.right(90)
    t.forward(300)

t.up()
t.right(90)
t.forward(150)
t.down()

for i in range(6):
    t.forward(90)
    t.left(70)
"""
t.mainloop()