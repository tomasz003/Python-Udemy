from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
LEFT_PLAYER_COLOR="deepskyblue"
RIGHT_PLAYER_COLOR="crimson"


screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle=Paddle(x_coord=-350,y_coord=0, pad_color=LEFT_PLAYER_COLOR)
r_paddle=Paddle(x_coord=350,y_coord=0, pad_color=RIGHT_PLAYER_COLOR)
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #bouncing off walls
    if abs(ball.ycor())>280:
        ball.bounce_walls()
    #bouncing off paddles
    if ball.distance(l_paddle)<53 and -350<ball.xcor()<-320 and ball.x_move<0 or ball.distance(r_paddle)<53 and 350>ball.xcor()>320 and ball.x_move>0:
        ball.bounce_paddles()
    #ball missed
    if ball.xcor()>400:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor()<-400:
        ball.reset_position()
        scoreboard.r_point()
    #winning
    if scoreboard.l_score==10:
        game_is_on=False
        scoreboard.winner("Left Player")

    if scoreboard.r_score==10:
        game_is_on=False
        scoreboard.winner("Right Player")

ball.hideturtle()
r_paddle.hideturtle()
l_paddle.hideturtle()
screen.update()

screen.exitonclick()