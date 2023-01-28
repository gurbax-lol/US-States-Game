import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].tolist()
game_is_on = True
guessed_states = []
score = 0


def check_state(guess):
    if guess.title() in list_of_states and guess.title() not in guessed_states:
        global score
        score += 1
        guessed_states.append(guess.title())
        return True
    else:
        return False


def format_title(game_score):
    if game_score == 0:
        return "Guess the state"
    else:
        return f"{game_score}/50 States Correct"


def plot_state(guessed_state):
    label = turtle.Turtle()
    state_series = data[data.state == guessed_state.title()]
    x_cor = int(state_series["x"])
    y_cor = int(state_series["y"])
    label.penup()
    label.hideturtle()
    label.goto(x_cor, y_cor)
    label.write(guessed_state.title(), move=False, align='left', font=('Arial', 8, 'normal'))


while game_is_on:
    answer_state = screen.textinput(title=f"{format_title(score)}", prompt="Name a US State!")
    if type(answer_state) is not str or answer_state.title() == "Exit":
        states_to_learn = [state for state in list_of_states if state not in guessed_states]
        df = pandas.DataFrame(states_to_learn, columns=["Learn these states: "])
        df.to_csv("states_to_learn.csv", index=False)
        break
    elif len(guessed_states) < len(list_of_states):
        if check_state(answer_state):
            plot_state(answer_state)
    else:
        game_is_on = False
