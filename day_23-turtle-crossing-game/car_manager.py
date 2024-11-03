from turtle import Turtle
from random import randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars=[]
        self.speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        if randint(1,5)==1:
            new_car=Turtle("square")
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(COLORS[randint(0, len(COLORS)-1)])
            new_car.goto(x=300, y=randint(-250,250))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed+=MOVE_INCREMENT




