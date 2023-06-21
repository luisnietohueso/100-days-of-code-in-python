from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 16, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')  # Set text color to white
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(0, 260)  # Position the turtle at the top center of the screen
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.write(arg='Game Over', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
