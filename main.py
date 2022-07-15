import turtle
from typing import List
import time
from snake_body import Snake
screen = turtle.Screen()
snake = Snake()
screen.setup(600,600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True
screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)






screen.exitonclick()


