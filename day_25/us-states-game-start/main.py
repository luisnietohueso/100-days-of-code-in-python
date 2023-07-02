import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
game_is_on = True
data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
number_guess = 0
coordinates = data[['x', 'y']]
guessed_states = []


def question():
    answer_state = screen.textinput(title=f'Guess the state {len(guessed_states)}/50',
                                    prompt="What's another state's name? ").title()
    answer_state_title = answer_state.title()
    return answer_state_title


while len(guessed_states) < 50:
    user_answer = question()

    if user_answer == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_cvs = pd.DataFrame(missing_states)
        new_cvs.to_csv('states_to_learn.cvs')
        break

    if user_answer.lower() or user_answer.upper() in all_states:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_answer)
        print(user_answer)
        number_guess += 1

# # states to learn.cvs
# all_states = [All_states]
# you_did_not_gues = set(all_states).difference(All_states)
# new_cvs = pd.DataFrame(you_did_not_gues)
# new_cvs.to_csv(f'len(guessed_states)')
# turtle.mainloop()
