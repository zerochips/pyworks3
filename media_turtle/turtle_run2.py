import turtle as t
import random

# 점수와 게임 스위치 변수
playing = False     # 게임 실행 상태 변수
score = 0           # 점수

# 적 거북이
te = t.Turtle()
te.shape('turtle')
te.color('red')
te.shapesize(1)
te.speed(0)
te.up()
te.goto(0, 200)

# 먹이
tf = t.Turtle()
tf.shape('circle')
tf.color('green')
tf.speed(0)
tf.up()
tf.goto(0, -200)

# 주인공 거북이
t.setup(500, 500)
t.bgcolor('orange')
t.shape('turtle')
t.speed(0)
t.up()
t.color('white')

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()   # 메시지를 지움
        play()

# 메시지를 화면에 표시하는 함수
def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()

def play():
    global score
    global playing

    if t.distance(te) < 12:
        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0

    if playing:
        t.ontimer(play, 100) # 0.1초 간격으로 계속 play

    # 거북이 기본 속도 설정
    t.forward(30)
    te.forward(5)

    # 적 거북이 반응 속도 제한 설정
    if random.randint(1, 5) == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)

    # 적 거북이 스피드 업 설정
    speed = score + 5
    if speed > 15:
        speed = 15
    te.forward(speed)

    size = score + 1
    if size > 15:
        size = 15
    te.turtlesize(size)

    if t.distance(tf) < 12:
        score = score + 1
        t.write(f'score: {score}')
        start_x = random.randint(-230, 230)
        start_y = random.randint(-230, 230)
        tf.goto(start_x, start_y)

# 키 조종
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, 'space')        # space 누르면 start 설정
t.listen()
message("Turtle Run", "[space]")

t.mainloop()