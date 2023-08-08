from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.goto(x=0, y=0)
        self.speed('slow')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        random_x = self.xcor() + self.x_move
        random_y = self.ycor() + self.y_move
        self.goto(random_x,random_y)
    
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
    
    def reset(self):
        self.goto(0,0)

        
