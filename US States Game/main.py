import turtle
import pandas

FONT = ()

screen = turtle.Screen()

data = pandas.read_csv("50_states.csv")

state_list = data["state"].tolist()

screen.title('U.S. State Game')
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

guessed_states = 0
game_is_active = True

while game_is_active:
    answer_state = screen.textinput(title=f"{guessed_states}/50 Guessed", prompt="Input the name of the state:")
    if answer_state.title() == "Exit":
        break
    for state in state_list:
        if state.lower() == answer_state.lower():
            guessed_states += 1
            state_text = turtle.Turtle()
            state_text.hideturtle()
            state_text.penup()
            x_cor = data.x[data.state == f"{state}"].item()
            y_cor = data.y[data.state == f"{state}"].item()
            state_text.goto(x_cor,y_cor)
            state_text.write(f"{state}", align="center", font=("Arial", 8, "normal"))
            state_list.remove(state)
        if guessed_states == 50:
            print("Wow!")
            game_is_active = False


new_csv = pandas.DataFrame(state_list, columns=["Unguessed States"])
new_csv.to_csv("not_guessed_states.csv")

turtle.mainloop()