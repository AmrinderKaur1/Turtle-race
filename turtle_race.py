from turtle import Screen, Turtle
import random
from tkinter import ttk

screen = Screen()
screen.listen()
turtle_list = []

user_bet = screen.textinput(title="make your bet!",
        prompt="Which turtle will win the race? Enter a color out of: red,blue,green,purple,orange,coral")

# print(user_bet)
is_race_on = False
clr_li = ["red", "blue", "green", "purple", "orange", "coral"]
y_cors = [100, 60, 20, -20, -60, -100]

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(clr_li[turtle_index])
    tim.goto(x=-230, y=y_cors[turtle_index])
    turtle_list.append(tim)


if user_bet:
    is_race_on = True

# screen.onkey(key="Enter", fun=is_race_on)

while is_race_on:
    for player in turtle_list:
        if player.xcor() > 200:
            is_race_on = False
            winning_turtle = player.pencolor()
            if winning_turtle == user_bet:
                print(f"you have won! The {winning_turtle} is the winner.")
                screen.textinput(title="You won 🎉🎉", prompt=f"The {winning_turtle} is the winner. Type an affirmation.👇")

            else:
                print(f"you have lost! The {winning_turtle} has won.")
                screen.textinput(title="You Lost 🙁🙁 ", prompt=f"The {winning_turtle} is the winner. Type an affirmation.👇")

        rand_dist = random.randint(0, 10)
        player.forward(rand_dist)


screen.exitonclick()
