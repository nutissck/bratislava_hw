from turtle import *
from tkinter import Button
screen = Screen()
screen.setup(width=600, height=600)
t=Turtle()
t.pensize(3)
t.pencolor("blue")
t.fillcolor("red")
def dopredu():
    t.forward(50)
def vpravo():
    t.right(90)
def vlavo():
    t.left(18)

button1=Button(text="Dopredu", command=dopredu)
button1.pack()

button2=Button(text="Vpravo", command=vpravo)
button2.pack()

button3=Button(text="Vľavo", command=vlavo)
button3.pack()

t.penup()
t.goto(-200, 200)
t.pendown()

for i in range(4):
    dopredu()
    dopredu()
    vpravo()
t.penup()
t.goto(-50, 200)
t.pendown()
for i in range(4):
    dopredu()
    dopredu()
    dopredu()
    vpravo()
t.penup()
t.goto(-200, 50)
t.pendown()
for i in range(5):
    dopredu()
    vpravo()
    vlavo()

t.penup()
t.goto(0, 0)
t.pendown()

for i in range(5):
    dopredu()
    vpravo()
    vlavo()

screen.mainloop()
