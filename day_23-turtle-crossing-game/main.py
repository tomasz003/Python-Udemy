import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()
cars=[]
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car(scoreboard.level)
    car_manager.move_cars()
    for car in car_manager.cars:
        if player.distance(car)<22:
            scoreboard.game_over()
            game_is_on=False
    if player.is_at_finish():
        player.restart()
        scoreboard.update_level()
        car_manager.level_up(scoreboard.level)

screen.exitonclick()