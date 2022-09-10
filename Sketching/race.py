from turtle import Screen, Turtle
import random
is_race_on = False

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(
    "Make your bet ", "Which turtle will win the race? ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []

for _ in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[_])
    tim.penup()
    tim.goto(x=-230, y=-70 + (_ * 30))
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print("You won")
            else:
                print(f"You lose. {winning_turtle} Won")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
