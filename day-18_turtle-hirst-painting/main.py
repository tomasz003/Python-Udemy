# import colorgram
# colors=colorgram.extract("spots.jpg",45)
# list_of_rgbs=[]
#
# for color in colors:
#     list_of_rgbs.append(tuple(color.rgb))
#
# print(list_of_rgbs)

from turtle import Turtle, Screen
from random import choice
color_list_rgb=[(1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165), (70, 70, 45), (185, 190, 201), (126, 225, 231), (88, 49, 45), (61, 65, 66)]

timmy=Turtle()
timmy.shape("arrow")
timmy.speed(0)
timmy.penup()
timmy.hideturtle()
screen=Screen()
screen.colormode(255)

for i in range(10):
    timmy.setposition(-275, -225+i*50)
    for j in range(10):
        col=choice(color_list_rgb)
        timmy.forward(50)
        timmy.dot(20, col)

screen.exitonclick()