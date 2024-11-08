import turtle
import pandas

screen=turtle.Screen()
screen.setup(width=700, height=500)
screen.title("USA States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states=pandas.read_csv("50_states.csv")
st_names=states.state.to_list()
guessed_states=[]

while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"Guess the State ({len(guessed_states)}/50)", prompt="What's another state's name").title()
    if answer_state == "Exit":
        missed_states = [states for states in st_names if states not in guessed_states]
        left_states=pandas.DataFrame(missed_states)
        left_states.to_csv("states_to_learn.csv")
        break
    if answer_state in st_names and answer_state not in guessed_states:
        drawing = turtle.Turtle()
        drawing.penup()
        drawing.hideturtle()
        x_cor=states[states.state==answer_state].x.item()
        y_cor=states[states.state==answer_state].y.item()
        drawing.goto(x_cor, y_cor)
        drawing.write(answer_state)
        guessed_states.append(answer_state)

