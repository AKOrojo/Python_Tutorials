from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score {self.score}", align=ALIGNMENT,
                   font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def gameover(self):
        self.goto(0, 0)
        self.write("Gameover", align=ALIGNMENT,
                   font=FONT)