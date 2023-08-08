from turtle import Turtle,Screen
from paddle_class import Paddle
from ball_class import Ball
from scoreboard_class import Scoreboard
import time

#Create the screen for game
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title("PONG")
screen.tracer(0)

#Create the ball
ball = Ball()

#create scoreboard
scoreboard= Scoreboard()
#create the paddle on the screen
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))


screen.listen()

#Move right paddle
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, 'Down')

#Move left paddle
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    #detect ball collision with the top of the wall
    if ball.ycor() > 280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect ball collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()> 330 or ball.distance(l_paddle) <50 and ball.xcor() <-330:
        ball.bounce_x()
    
    #detect if the right paddle miss the ball
    if ball.xcor()>380:
        ball.reset()
        scoreboard.l_point()
    
    #detect if left paddle misses
    if ball.xcor()<-380:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()  # exitonclick is used to close the screen after clicking somewhere on screen
