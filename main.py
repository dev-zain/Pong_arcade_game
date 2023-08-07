from turtle import Turtle,Screen
from paddle_class import Paddle

#Create the square shape
# shape = Turtle('square')
# shape.color('white')

#Create the screen for game
screen = Screen()
screen.bgcolor('black')
screen.setup(width=700,height=600)
screen.title("PONG")
screen.tracer(0)

#create the paddle on the screen
r_paddle = Paddle((300,0))
l_paddle = Paddle((-300,0))


screen.listen()

#Move right paddle
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, 'Down')

#Move left paddle
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, 's')

game_is_on = True

while game_is_on:
    screen.update()
screen.exitonclick()  # exitonclick is used to close the screen after clicking somewhere on screen
