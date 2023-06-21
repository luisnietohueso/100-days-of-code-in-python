from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake game')
screen.tracer(0)

position = [-40, -20, 0]
segments = []

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.Up, 'Up')
screen.onkey(snake.Down, 'Down')
screen.onkey(snake.Left, 'Left')
screen.onkey(snake.Right, 'Right')
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect coalition
    if snake.head.distance(food) < 15:
        print('nom nom')

screen.exitonclick()
