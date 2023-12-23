import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ').lower()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
x, y = -230, -100
turtle_racers = []


for color in colors:
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    y = y+30
    new_turtle.goto(x, y)
    turtle_racers.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_racer in turtle_racers:
        if turtle_racer.xcor() > 230:
            is_race_on = False
            winning_color = turtle_racer.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_steps = random.randint(0,10)
        turtle_racer.fd(random_steps)

screen.exitonclick()
