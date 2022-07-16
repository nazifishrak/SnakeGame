
from turtle import Turtle


FONT = ('Courier', 15, "bold")
ALIGN = 'center'

class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0,250)
        self.write(f'SCORE: {self.score}',align = ALIGN, font = FONT)

    def increase_score(self):
        self.clear()
        self.score +=1
        self.write(f'Score: {self.score}',align= ALIGN, font = FONT)
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.color('red')
        self.write("GAME OVER", align= ALIGN, font = FONT)
        self.goto(0,-25)
        self.color('white')
        self.write(f'Score: {self.score}',align= ALIGN, font = FONT)




