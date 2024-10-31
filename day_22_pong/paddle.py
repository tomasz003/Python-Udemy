from turtle import Turtle
MOVE_DIST=20
UP=90
DOWN=270

class Paddle(Turtle):
    def __init__(self, x_coord,y_coord, pad_color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.goto(x_coord, y_coord)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(pad_color)
    def up(self):
        if self.ycor()<250:
            new_y = self.ycor()+MOVE_DIST
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -240:
            new_y=self.ycor()-MOVE_DIST
            self.goto(self.xcor(), new_y)

