import turtle as t
import random

"""for _ in range(4):
    tim.forward(100)
    tim.end_fill()
    tim.left(90)
    tim.pendown()
"""

"""for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()"""

"""def draw_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.right(angle)


for side in range(3, 11):
    draw_shape(side)
    tim.color(random.choice(color))"""

"""for _ in range(200):
    tim.color(randon_color())
    tim.forward(30)
    tim.setheading(random.choice(positions))
"""
t.colormode(255)


def randon_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color = (r, g, b)
    return color


tim = t.Turtle()
tim.shape('turtle')
tim.color('coral')
positions = [0, 90, 180, 270]
tim.pensize(1)
tim.speed("fastest")

"""for _ in range(180):
    tim.color(randon_color())
    tim.left(2)
    tim.circle(100)
"""


def draw_spirograhp(size_gap):
    for _ in range(int(360 / size_gap)):
        tim.color(randon_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_gap)


draw_spirograhp(6)

screen = t.Screen()
screen.exitonclick()
