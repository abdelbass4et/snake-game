from pickle import FALSE
from random import random
import time
from food import food
from  turtle import Turtle,Screen
from snake import SNAKE
from score import score
window = Screen()
window.bgcolor('black')
window.setup(width=800,height=800)
window.tracer(0)
score = score()
worm =  SNAKE()
point = food()
window.update()
run_game=True
while run_game:
    worm.move_snake()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(worm.move_up,'Up')
    window.onkey(worm.move_down,'Down')
    window.onkey(worm.move_right,'Right')
    window.onkey(worm.move_left,'Left')
    if worm.head.distance(point)<15:
        point.random_position()
        worm.extend()
        score.update_score()
    if worm.head.xcor() > 370 or worm.head.xcor() <-370 or worm.head.ycor() > 370 or worm.head.ycor() < -370:
        run_game= False
        score.game_over()
    for squar in worm.snakes[:-1]:
        if worm.head.distance(squar)<10:
            run_game=False
            score.game_over()
window.exitonclick()