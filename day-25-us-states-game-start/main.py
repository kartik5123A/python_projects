import turtle
import pandas

screen = turtle.Screen()
screen.setup(height = 550, width = 780)
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# to get states cordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)    
# turtle.mainloop()

# load data from csv
states_data = pandas.read_csv("50_states.csv")

guessed_states = []

# search if the state is list
while len(guessed_states) < 50:
      states = states_data["state"].to_list()

      # input block
      answer_state = turtle.textinput(title = f"{len(guessed_states)}/50 correct Guess next state", prompt = "Enter your guessed state : ").title()

      if answer_state == "Exit":
          #  missing_state = []
          #  for state in states:
          #       if state not in guessed_states:
          #            missing_state.append(state)
           missing_state = [state for state in states if state not in guessed_states]
           new_data = pandas.DataFrame(missing_state)
           new_data.to_csv("states_to_learn.csv")       
           break
      
      if answer_state in states:
         t = turtle.Turtle()
         t.hideturtle()
         t.penup()
         state_data = states_data[states_data.state == answer_state]
         t.goto(int(state_data.x), int(state_data.y))
         t.write(state_data.state.item())
         guessed_states.append(answer_state)
