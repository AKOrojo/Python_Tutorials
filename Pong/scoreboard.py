from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"{self.score1} Score {self.score2}", align=ALIGNMENT,
                   font=FONT)

    def update1(self):
        self.score1 += 1
        self.clear()
        self.update_scoreboard()

    def update2(self):
        self.score2 += 1
        self.clear()
        self.update_scoreboard()

    def gameover(self):
        self.goto(0, 0)
        self.write("Gameover", align=ALIGNMENT,
                   font=FONT)
