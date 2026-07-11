from turtle import *
from random import *

screen= Screen()
screen.setup(width=500, height=500)
#текст заголовку
label=Turtle()
label.penup()
label.hideturtle()
label.goto(0,170)
label.color("red")
label.write("turtle racing", font=("Arial", 20, "normal"), align="center")
#track
speed(150)
penup()
goto(-140,140)
for i in range(15):
    write(i, align="center")
    right(90)
    forward(10)
    pendown()
    for i in range(8):
        forward(10)
        penup()
        forward(10)
        pendown()
    penup()
    backward(170)
    left(90)
    forward(20)
write("finish")
pendown()
width(3)
color("red")
right(90)
forward(160)
hideturtle()
#черепашки бігуни
colors=["red", "yellow", "green", "blue"]
positions=[100, 70, 40, 10]
turtles=[]
for i in range(4):
    t=Turtle()
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-160, positions[i])
    turtles.append(t)
a=turtles[0]
b=turtles[1]
c=turtles[2]
d=turtles[3]

#gonka
for turn in range(115):
    for t in turtles:
        t.forward(randint(0,5))

#визначаем переможця
max_x=a.xcor()#припустимо що це переможець
max_l=a
if b.xcor()>max_x:
    max_x=b.xcor()
    max_l=b
if c.xcor()>max_x:
    max_x=c.xcor()
    max_l=c
if d.xcor()>max_x:
    max_x=d.xcor()
    max_l=d
#результат
label.goto(0,-170)
max_l.goto(0,-175)
label.write(f"winner {int(max_x)}", font=("Arial", 20, "normal"), align="center")


screen.mainloop()