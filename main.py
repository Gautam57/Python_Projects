import turtle
import pandas

screen = turtle.Screen()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state = data.state.to_list()
X = data.x.to_list()
Y = data.y.to_list()
guessed_states = []
missed_states = []

correct = 0
while correct <= 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name? ").title()
    if answer_state == 'Exit':
        for s in state:
            if s not in guessed_states:
                missed_states.append(s)
            missed_data = pandas.DataFrame(missed_states)
            missed_data.to_csv("missed states")
        break

    for s in state:
        if s == answer_state:
            i = state.index(answer_state)
            t = turtle.Turtle()
            new_x = X[i]
            new_y = Y[i]
            t.hideturtle()
            t.penup()
            t.goto(new_x, new_y)
            t.write(s)
            correct += 1
            guessed_states.append(answer_state)
    screen.title(f"{correct}/50 U.S. States Game")

screen.exitonclick()



