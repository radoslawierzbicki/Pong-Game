import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

#position Ball
ball = Ball((0, 0))

scoreboard = Scoreboard()
screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce()

    # Detect R paddle misses
    if ball.xcor() > 410:
        ball.reset_position()
        scoreboard.l_point()
        time.sleep(2)

    # Detect L paddle misses
    if ball.xcor() < -410:
        ball.reset_position()
        scoreboard.r_point()
        time.sleep(2)


screen.exitonclick()

