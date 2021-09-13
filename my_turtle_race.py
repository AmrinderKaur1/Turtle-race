from turtle import Turtle, Screen
import random

new_turtle = Turtle(shape="turtle")
new_turtle.hideturtle()
screen = Screen()
screen.setup(width=640, height=600)
text_x_axes = [-270, -214, -158, -102, -46, 10, 66, 122, 178, 234]
track_y_axes= [240, 180, 120, 60, 0, -60, -120, -180, -240]
new_turtle.speed("fastest")
turtle_y_axes = [210, 150, 90, 30, -30, -90, -150, -210,-270]
is_race_on = False
turtle_colors = ["red", "blue", "orange", "purple", "green", "black", "brown", "pink"]
turtle_list = []
user_bet = screen.textinput(title="make your bet!",
                            prompt="Who will win? red,blue,orange,purple,green,black,brown,pink?")
screen.listen()
if user_bet:
    is_race_on = True
else:
    screen.bye()


def text():
    new_turtle.penup()
    for i in range(1,11):
        new_turtle.goto(text_x_axes[i-1], 270)
        new_turtle.write(i, font=10)
text()


def drawing_track():
    new_turtle.penup()
    for j in range(0,9):
        new_turtle.goto(-270,track_y_axes[j])
        for i in range(0,7):
            new_turtle.pendown()
            new_turtle.forward(55)
            new_turtle.penup()
            new_turtle.forward(25)
drawing_track()


def turtle_setup():
     for i in range(0,8):
        timms = Turtle(shape="turtle")
        timms.penup()
        timms.color(turtle_colors[i])
        timms.goto(x=-270, y=turtle_y_axes[i])
        timms.speed("normal")
        for j in range(0, 10):
            timms.right(36)
        turtle_list.append(timms)
        timms.pendown()
turtle_setup()


def turtle_movement():
    is_race_on = True
    while is_race_on:
         for player in turtle_list:
             if player.xcor() > 249:
                 is_race_on = False
                 winning_turtle = player.pencolor()
                 if winning_turtle == user_bet:
                    print(f"You have won! The {winning_turtle} is the winner.")
                    screen.textinput(title="You won 🎉🎉",
                                  prompt=f"The {winning_turtle} is the winner.Type an affirmation.👇")
                 else:
                     print(f"You have lost! The {winning_turtle} is the winner.")
                     screen.textinput(title="You Lost 🙁🙁 ",
                                 prompt=f"The {winning_turtle} is the winner. Type an affirmation.👇")
             rand_dist = random.randint(0,10)
             player.forward(rand_dist)


start_race = screen.textinput(title="Shall we start?",
                              prompt="(Yes/No) If Yes, Press OK.")

if start_race.title()=="Yes":
    turtle_movement()
else:
    screen.bye()

screen.exitonclick()
