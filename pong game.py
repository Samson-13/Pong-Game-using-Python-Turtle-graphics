# Made by M Samson Badding
# if the ball speed is too fast or slow change it in the ball section
# Welcome to the pong game

import turtle

# FOr Stick A
def stickAfun():
    win.onkeypress(stickAfun, 'w')
    win.onkeypress(stickAfun, 's')
    if win.onkeypress(moverW, 'w'):
        pass
    if win.onkeypress(moverS, 's'):
        pass

# Movement Up for Stick A
def moverW():
    y = stickA.ycor()
    y += 23
    stickA.sety(y)

# Movement Down for Stick A
def moverS():
    y = stickA.ycor()
    y -= 23
    stickA.sety(y)


# FOr Stick B
def stickBfun():
    win.onkeypress(stickBfun, 'Up')
    win.onkeypress(stickBfun, 'Down')
    if win.onkeypress(moverUp, 'Up'):
        pass
    if win.onkeypress(moverDown, 'Down'):
        pass


# Movement Up for Stick A
def moverUp():
    y = stickB.ycor()
    y += 23
    stickB.sety(y)


# Movement Down for Stick A
def moverDown():
    y = stickB.ycor()
    y -= 23
    stickB.sety(y)

# Border collision bounce
def  borderCorner():
    if ball.ycor() > 290:
        borderYa()
    if ball.ycor() < -290:
        borderYb()

# Ball bounces back
def borderYa():
    ball.sety(290)
    ball.dy *= -1

# Ball bounces back
def borderYb():
    ball.sety(-290)
    ball.dy *= -1

# stick doesn't goes past the windows height
def stick(stickA, stickB):
    if stickA.ycor() > 260:
        stickA.sety(260)
    if stickA.ycor() < -250:
        stickA.sety(-250)
    if stickB.ycor() > 260:
        stickB.sety(260)
    if stickB.ycor() < -250:
        stickB.sety(-250)

# Main code
# Score Board
scoreA = 0
scoreB = 0

# Score Reader
scoreRead = turtle.Turtle()
scoreRead.speed(0)
scoreRead.color('white')
scoreRead.penup()
scoreRead.hideturtle()
scoreRead.goto(0, 260)
scoreRead.write('Player A: {}  Player B: {}'.format(scoreA, scoreB), align='center', font=('Courier', 24,'normal'))

# window's size
win = turtle.Screen()
win.title('Samson\'s Pong Game')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

# Stick A
stickA = turtle.Turtle()
stickA.speed(0)
stickA.shape('square')
stickA.color('orange')
stickA.shapesize(stretch_wid=5, stretch_len=1)
stickA.penup()
stickA.goto(-350, 0)

# Stick B
stickB = turtle.Turtle()
stickB.speed(0)
stickB.shape('square')
stickB.color('green')
stickB.shapesize(stretch_wid=5, stretch_len=1)
stickB.penup()
stickB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
# ball speed (Change if yr ball is too fast or slow)
ball.dx = 0.2
ball.dy = -0.2


# real
win.listen()
stickAfun()
stickBfun()

while True:
    win.update()

    # mover ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Stick function
    stick(stickA, stickB)

    # ball border bounce
    borderCorner()
    # Score Counter
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        scoreRead.clear()
        scoreRead.write('Player A: {}  Player B: {}'.format(scoreA, scoreB), align='center', font=('Courier', 24, 'normal'))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        scoreRead.clear()
        scoreRead.write('Player A: {}  Player B: {}'.format(scoreA, scoreB), align='center', font=('Courier', 24, 'normal'))


    if (ball.xcor() > 330) and (ball.xcor() < 340) and (ball.ycor() < stickB.ycor() + 40) and (ball.ycor() > stickB.ycor() - 40):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -330) and (ball.xcor() > -340) and (ball.ycor() < stickA.ycor() + 40) and (ball.ycor() > stickA.ycor() - 40):
        ball.setx(-330)
        ball.dx *= -1