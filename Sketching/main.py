from turtle import Screen, Turtle
import random

tim = Turtle()
screen = Screen()

screen.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_clock():
    tim.right(10)


def move_anti_clock():
    tim.left(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_clock)
screen.onkey(key="a", fun=move_anti_clock)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
