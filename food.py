
from turtle import Turtle, penup

import random
class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.shapesize(0.5,0.5)
        self.random_position()
        
        
    def random_position(self):
        random_x= random.randint(-390,390)
        random_y= random.randint(-390,390)
        self.goto(random_x,random_y)
    