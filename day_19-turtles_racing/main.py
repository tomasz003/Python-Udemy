from turtle import Turtle, Screen
import random
is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors=["red", "yellow", "orange", "green", "blue", "purple"]
all_turtles=[]

for turtle_index in range(len(colors)):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, 105-30*turtle_index)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")
        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)


screen.exitonclick()


# def w_move():
#     tim.forward(10)
# screen.onkey(key="w", fun=w_move)
