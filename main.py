import turtle
from typing import List
import time
from food import Food
from scoreboard import ScoreBoard
from snake_body import Snake
screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = ScoreBoard()

game_is_on = True
screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.05)

    # Detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        score_board.increase_score()
    
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    if x_cor>=290 or x_cor <=-290 or y_cor>=290 or y_cor<=-290:
        game_is_on = False
        score_board.game_over()

    for box in snake.boxes[1::]:
        if snake.head.distance(box) <= 15:
            game_is_on = False
            score_board.game_over()
            







screen.exitonclick()


