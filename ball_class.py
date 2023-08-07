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

    def move_ball(self):
        random_x = self.xcor() + 10
        random_y = self.ycor() + 10
        self.goto(random_x,random_y)
        
