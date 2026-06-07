from turtle import Turtle

class score(Turtle): # Class names should ideally be capitalized
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 350) # Adjusted Y-coordinate (370 is often off-screen)
        self.hideturtle()
        self.print_score() # Print initial score without incrementing it first

    def print_score(self):
        self.clear() # Clear only this specific turtle's drawings
        # Fixed the font tuple syntax below
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'bold'))

    def update_score(self):
        self.score += 1 
        self.print_score()    

    def game_over(self):
        self.screen.bgcolor('red')
        self.goto(0, 0)
        # Fixed "YOU" to "YOUR"
        self.write(f'GAME OVER!! \n YOUR SCORE IS : {self.score}', align='center', font=('Arial', 30, 'normal'))