from turtle import Turtle, Screen



screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet?", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_possitions = [-70, -40, -10, 20, 50, 80]


for turtle_index in range(0, 6):
    nina = Turtle("turtle")
    nina.color(colors[turtle_index])
    nina.penup()
    nina.goto(x=-239, y=y_possitions[turtle_index])








screen.exitonclick()