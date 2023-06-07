"""
races of turtle in this code will be code a video game about a races
"""
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make a bet', prompt='Which Turtle will win the race? Enter a color:')
all_turtle = []
print(user_bet)
colors = ['red', 'orange', 'yellow', 'purple', 'green', 'blue']
Y_position = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(0, 6):
    turtle = Turtle(shape='turtle')
    turtle.penup()
    turtle.goto(x=-230, y=Y_position[turtle_index])
    turtle.color(colors[turtle_index])
    all_turtle.append(turtle)

if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You won! The winning is {winning_color} ')
            else:
                print(f'You lost! The winning is {winning_color}')

            print(turtle.pencolor())
        random_distances = random.randint(0, 10)
        turtle.forward(random_distances)

screen.exitonclick()
