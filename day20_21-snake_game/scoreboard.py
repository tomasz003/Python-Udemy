from turtle import Turtle
ALIGN="center"
FONT=("Courier", 17, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 265)
        self.color("white")
        self.score=0
        with open("data.txt") as data:
            self.highscore=int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore: {self.highscore}", align=ALIGN, font=FONT)

    #def game_over(self):
    #    self.goto(0,0)
    #    self.write("Game Over.", align=ALIGN, font=FONT)

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.score=0
        self.update_scoreboard()
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
