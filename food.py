from random import randint
import turtle


class Food(turtle.Turtle):
    
    def __init__(self) -> None:
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid= 0.5)
        self.color("pink")
        self.speed(0)
        self.refresh()


    def refresh(self):
        random_x =  randint(-280,280)
        random_y =  randint(-280,240)
        self.goto(random_x,random_y)


