from turtle import Screen, Turtle
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

sides = [3, 4, 5, 6, 7, 8, 9, 10]
colour = ["red", "blue", "green", "purple"]


for side in sides:
    for _ in range(side):
        tim.forward(100)
        tim.right(360/side)
    tim.color(random.choice(colour))


for _ in range(4):
    tim.forward(100)
    tim.right(90)

tim.left(90)
for _ in range(15):
    tim.penup()
    tim.forward(10)
    tim.pendown()
    tim.forward(10)

screen = Screen()
screen.exitonclick()
