import turtle as t

import random

screen = t.Screen()

screen.setup(width = 500, height = 400)

is_race_on = False

user_bet = screen.textinput(title = "Make a Bet", prompt = "Choose your turtle?? Enter a color : ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_index = [-150, -90, -30, 30, 90, 150]

all_turtles = []

for turtle_index in range(0, 6):

    new_turtle = t.Turtle(shape = "turtle")

    new_turtle.color(colors[turtle_index])

    new_turtle.penup()

    new_turtle.goto(x = -230, y = y_index[turtle_index])

    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True  
     
while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False  
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} is the winner.")
            else:
                print(f"You have lost! The {winning_color} is the winner.")    
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()