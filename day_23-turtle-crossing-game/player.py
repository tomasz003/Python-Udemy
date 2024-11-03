from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.shape("turtle")
        self.speed("fastest")
        self.setheading(90)
        self.restart()

    def move(self):
        self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def is_at_finish(self):
        if self.ycor()>=FINISH_LINE_Y:
            return True
        else:
            return False

    def restart(self):
        self.goto(STARTING_POSITION)

