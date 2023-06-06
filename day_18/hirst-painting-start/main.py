###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
"""import turtle as t
import random

color_list = [(245 / 255, 243 / 255, 238 / 255), (246 / 255, 242 / 255, 244 / 255), (202 / 255, 164 / 255, 110 / 255),
              (240 / 255, 245 / 255, 241 / 255), (236 / 255, 239 / 255, 243 / 255), (149 / 255, 75 / 255, 50 / 255),
              (222 / 255, 201 / 255, 136 / 255), (53 / 255, 93 / 255, 123 / 255), (170 / 255, 154 / 255, 41 / 255),
              (138 / 255, 31 / 255, 20 / 255), (134 / 255, 163 / 255, 184 / 255), (197 / 255, 92 / 255, 73 / 255),
              (47 / 255, 121 / 255, 86 / 255), (73 / 255, 43 / 255, 35 / 255), (145 / 255, 178 / 255, 149 / 255),
              (14 / 255, 98 / 255, 70 / 255), (232 / 255, 176 / 255, 165 / 255), (160 / 255, 142 / 255, 158 / 255),
              (54 / 255, 45 / 255, 50 / 255), (101 / 255, 75 / 255, 77 / 255), (183 / 255, 205 / 255, 171 / 255),
              (36 / 255, 60 / 255, 74 / 255), (19 / 255, 86 / 255, 89 / 255), (82 / 255, 148 / 255, 129 / 255),
              (147 / 255, 17 / 255, 19 / 255),
              (27 / 255, 68 / 255, 102 / 255), (12 / 255, 70 / 255, 64 / 255), (107 / 255, 127 / 255, 153 / 255),
              (176 / 255, 192 / 255, 208 / 255), (168 / 255, 99 / 255, 102 / 255)]

turtle = t.Turtle()
turtle.pensize(9)
turtle.dot(20,random.choice(color_list))
x = 0
y = 0


def move():
    for _ in range(10):
        turtle.forward(0)
        turtle.penup()
        turtle.forward(25)
        turtle.pendown()


def position():
    turtle.penup()
    turtle.backward(500)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(90)
    turtle.pendown()


for _ in range(10):
    move()
    position()
    move()"""
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()