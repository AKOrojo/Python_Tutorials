from turtle import Screen, distance
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up_alt, "w")
screen.onkey(l_paddle.down_alt, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 350:
        ball.reset_place()
        scoreboard.update1()

    elif ball.xcor() < -350:
        ball.reset_place()
        scoreboard.update2()

screen.exitonclick()
