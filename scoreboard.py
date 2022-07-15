import turtle
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.Scorevalue = 0
        self.high_score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        if self.Scorevalue>self.high_score:
            self.high_score=self.Scorevalue
            with open("data.txt",mode="w") as file:
                file.write(str(self.high_score))
        with open("data.txt") as file:
            self.high_score=int(file.read())
        self.write(f"Score: {self.Scorevalue}  High Score : {self.high_score}",align="center", font=("Arial",20,"normal"))



    def scoreRefresh(self):
             self.Scorevalue+=1
             self.clear()
             self.update_scoreboard()

    def reset(self):
        if self.Scorevalue>self.high_score:
            self.high_score=self.Scorevalue
        self.Scorevalue=0
        self.update_scoreboard()





