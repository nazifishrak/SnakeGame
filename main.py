import turtle
from typing import List
import time
from food import Food
from scoreboard import ScoreBoard
from snake_body import Snake







def main():
    # *************************************** SCREEN SETUP*************************
    screen = turtle.Screen()
    screen.clear()
    screen.setup(600,600)
    screen.bgcolor('black')
    screen.title("Snake Game")
    screen.tracer(0)
    
    # **********************Setting time delay of graphics based on easy/hard game level**************
    user_difficulty = screen.textinput("Choose Difficulty Level", "easy/hard")
    # snake_color = screen.textinput("Choose Snake Color", "type color name e.g pink, blue, white etc")
    if user_difficulty.lower() == 'easy':
        user_difficulty = 0.1
    else:   
        user_difficulty = 0.05
    
    # ***************************CREATING OBJECTS***********************************
    snake = Snake()
    food = Food()
    score_board = ScoreBoard()


    # **********************GAME FLOW LOGIC*************************************
    game_is_on = True
    screen.listen()
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.down, "Down")
    while game_is_on:
        screen.update()
        snake.move()
        time.sleep(user_difficulty)

        # Detect collision with food

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.grow()
            score_board.increase_score()
        
        # Detect collison with wall
        x_cor = snake.head.xcor()
        y_cor = snake.head.ycor()
        if x_cor>=290 or x_cor <=-290 or y_cor>=290 or y_cor<=-290:
            game_is_on = False
            score_board.game_over()
        # Detect collision with own body
        for box in snake.boxes[1::]: # Ignores the first posistion of the snake head
            if snake.head.distance(box) <= 15:
                game_is_on = False
                score_board.game_over()
    play_again = screen.textinput("Try again?", "yes/no")
    if play_again.lower() == 'yes':
        main()
    else:   
        pass

main()










