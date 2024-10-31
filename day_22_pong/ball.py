from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x_move=4
        self.y_move=4
        self.move_speed=0.015

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def bounce_walls(self):
        self.y_move*=-1

    def bounce_paddles(self):
        self.x_move*=-1
        self.move_speed*=0.8

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_paddles()
        self.move_speed=0.015

