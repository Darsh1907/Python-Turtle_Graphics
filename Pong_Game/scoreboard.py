from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboad()

    def update_scoreboad(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Times New Roman", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Times New Roman", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboad()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboad()