import colorgram
from turtle import Turtle, Screen
import random
colours = colorgram.extract('spot.jpg',14)
alist = []
for i in range(len(colours)):
    alist.append(tuple(colours[i].rgb))
alist.pop(0)

t = Turtle()
screen = Screen()
screen.colormode(255)
t.speed('fastest')
y = -150
t.penup()
t.sety(y)
t.setx(-150)
t.hideturtle()
for i in range(10):
    for j in range(10):
        col = random.choice(alist)

        t.pencolor(col)
        t.dot(20, col)

        t.forward(50)

    t.penup()
    t.setx(-150)
    y+= 50
    t.sety(y)






screen.exitonclick()