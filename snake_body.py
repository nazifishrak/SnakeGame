
import turtle
from typing import List


STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]

UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self) -> None:
        self.boxes: List[turtle.Turtle] = []
        self.create_snake()
        self.head: turtle.Turtle = self.boxes[0]
    
    def create_snake(self):
        for i in STARTING_POSITIONS:
            box = turtle.Turtle('square')
            box.pu()
            box.color('orange')
            box.goto(i)
            self.boxes.append(box)
    def up(self):
        if self.head.heading() != DOWN:    
            self.head.setheading(UP)
    def right(self):
        if self.head.heading() != LEFT:    
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:    
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
   
    def move(self):
        for box_num in range(len(self.boxes)-1, 0, -1):
            new_x = self.boxes[box_num-1].xcor()
            new_y = self.boxes[box_num-1].ycor()
            self.boxes[box_num].goto(new_x,new_y)     
        self.head.forward(20)
        




