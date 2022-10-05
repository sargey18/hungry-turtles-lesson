import turtle
import random

window = turtle.Screen()
window.setup(400, 400)
window.bgcolor("sky blue")
window.tracer(0)

fred = turtle.Turtle()
fred.color("red")
fred.penup()
fred.shape("turtle")

ball = turtle.Turtle()
ball.shape("circle")
ball.penup()
ball.color("green")

def move_ball():
    ball.setx(random.randint(-180, 180))
    ball.sety(random.randint(-180, 180))


def move_left():
    fred.left(90)

def move_right():
    fred.right(90)

def teleport():
    if fred.xcor() > 200 or fred.xcor() < -200:
        fred.setx(-fred.xcor())

    if fred.ycor() > 200 or fred.ycor() < -200:
        fred.sety(-fred.ycor())

window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.listen()

move_ball()

while True:
    fred.forward(0.05)

    teleport()

    if fred.distance(ball) < 20:
        ball.clear()
        move_ball()
    window.update()

turtle.done()