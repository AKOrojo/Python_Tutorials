from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down_alt(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def up_alt(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
