from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(100)


def move_bacwards():
    tim.backward(100)


def move_counter():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clean():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_bacwards)
screen.onkey(key='a', fun=move_counter)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='c', fun=clean)
screen.exitonclick()
