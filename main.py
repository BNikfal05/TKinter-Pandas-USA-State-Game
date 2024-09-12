import turtle
import pandas

SCREEN_WIDTH = 725
SCREEN_HEIGHT = 491
FILE_NAME = '50_states.csv'
IMAGE = 'blank_states_img.gif'
AMOUNT_OF_STATES = 50

screen = turtle.Screen()
screen.title('U.S. States Game')
screen.addshape(IMAGE)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
turtle.shape(IMAGE)

data = pandas.read_csv(FILE_NAME)
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < AMOUNT_OF_STATES:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{AMOUNT_OF_STATES} States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        states_to_learn = [
            state for state in all_states if state not in guessed_states]
        df = pandas.DataFrame(states_to_learn)
        df.to_csv('States_to_learn.csv')

        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # .item() grabs the first item/value under state_date.state
        t.write(answer_state)


# Challenges:
# 1. Exctracting data from a CSV file using pandas
#    a) Getting the state name or x-y coordinates specfically
# Solution: Going on the Pandas documentation and control f'ing the solution
# 2. Getting the coordinates for the states
# Solution: Utilizing a function that provides the x-y coordinates of a mouse click then storing it on an excel file found through StackOverflow
# 3. Structurally whether to make different class files but it was not necessary for this application
# 4. What to do when user capitalizes or not the first letter of their input
# Solution: User .title() method to capitalize the first letter of their response, found through ChatGPT
