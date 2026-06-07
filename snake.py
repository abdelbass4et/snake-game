from turtle import Turtle, position
import random
import time
class SNAKE:
    def __init__(self):
        self.snakes=[]
        self.positions=[(-80,0),(-60,0),(-40,0),(-20,0),(0,0)]
        self.create_snake()
        self.head= self.snakes[-1]
        
        
    def create_snake(self):
        for x in range(len(self.positions)):
            
            new_turtle = Turtle('square')
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.goto(self.positions[x]) 
            self.snakes.append(new_turtle)
        
            
    def move_snake(self):
       
        for x in range(len(self.snakes)-1):
            self.snakes[x].goto(self.snakes[x+1].pos())
        self.snakes[-1].forward(20)
        
        
    def move_up(self):
        self.head.setheading(90)
    def move_down(self):
        self.head.setheading(270)
    def move_right(self):
        self.head.setheading(0)
    def move_left(self):
        self.head.setheading(180)
    
    
    def extend(self):
        new_square = Turtle('square')
        new_square.color('white')
        new_square.penup()
        new_square.goto(self.snakes[0].pos())
        self.snakes.insert(0,new_square)
        