from turtle import Turtle

class score(Turtle): 
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 350)
        self.hideturtle()
        self.print_score() 

    def print_score(self):
        self.clear() 
        
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'bold'))

    def update_score(self):
        self.score += 1 
        self.print_score()    

    def game_over(self):
        self.screen.bgcolor('red')
        self.goto(0, 0)
       
        self.write(f'GAME OVER!! \n YOUR SCORE IS : {self.score}', align='center', font=('Arial', 30, 'normal'))
