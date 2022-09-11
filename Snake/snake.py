from turtle import Turtle, position

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.all_turtle = []
        self.create_snake()
        self.head = self.all_turtle[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_turtle(position)

    def move(self):
        for tut_num in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[tut_num - 1].xcor()
            new_y = self.all_turtle[tut_num - 1].ycor()
            self.all_turtle[tut_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def add_turtle(self, position):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("white")
        tim.goto(position)
        self.all_turtle.append(tim)

    def extend(self):
        self.add_turtle(self.all_turtle[-1].position())
