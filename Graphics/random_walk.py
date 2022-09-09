import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

########### Challenge 4 - Random Walk ########
directions = [0, 90, 180, 270]
tim.pensize(4)
tim.speed("fastest")


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def sizecc(size):
    for _ in range(int(360/size)):
        tim.pencolor(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size)


sizecc(10)

screen = Screen()
screen.exitonclick()
