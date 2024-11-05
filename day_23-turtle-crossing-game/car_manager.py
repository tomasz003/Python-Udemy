from turtle import Turtle
from random import randint, choice
COLORS = [ "darkred", "chocolate", "yellow", "darkgreen", "teal", "indigo", "dimgray", "dimgray"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars=[]
        self.speed=STARTING_MOVE_DISTANCE

    def create_car(self,level):
        if randint(0,max((80-5*level),30))<15:
            new_car=Turtle("square")
            new_car.penup()
            new_car.shape("square")
            col_choice=randint(0, len(COLORS) - 1)
            new_car.color(COLORS[col_choice])
            new_car.shapesize(stretch_wid=0.85, stretch_len=2+(COLORS[col_choice]=="dimgray"))
            new_car.left_or_right=choice([-1,1])
            new_car.goto(x=new_car.left_or_right*300, y=randint(-12,13)*20)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.goto(x=car.xcor()-self.speed*car.left_or_right, y=car.ycor())

    def level_up(self, level):
        self.speed+=MOVE_INCREMENT/level




