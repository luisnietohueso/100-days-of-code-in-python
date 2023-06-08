from turtle import Turtle

position = [-40, -20, 0]
moving = 20
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.snake_creation()

    def snake_creation(self):
        for turtle_index in range(0, 3):
            snake = Turtle('square')
            snake.penup()
            snake.color('white')
            snake.goto(x=position[turtle_index], y=0)
            self.segments.append(snake)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(moving)

    def Left(self):
        if self.segments[0].heading() != left:
            self.segments[0].setheading(left)

    def Right(self):
        if self.segments[0].heading() != right:
            self.segments[0].setheading(right)

    def Up(self):
        if self.segments[0].heading() != up:
            self.segments[0].setheading(up)

    def Down(self):
        if self.segments[0].heading() != down:
            self.segments[0].setheading(down)
