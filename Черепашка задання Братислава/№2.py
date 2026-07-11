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
def begin():
    t.begin_fill()
def end():
    t.end_fill()

button1=Button(text="Dopredu", command=dopredu)
button1.pack()

button2=Button(text="Vpravo", command=vpravo)
button2.pack()

button3=Button(text="Vľavo", command=vlavo)
button3.pack()

Button(text="begin", command=begin).pack()
Button(text="end", command=end).pack()

t.penup()
t.goto(-200, 200)
t.pendown()

begin()

for i in range(5):
    dopredu()
    vpravo()
    vlavo()

end()

t.penup()
t.goto(-50, 200)
t.pendown()

begin()

for i in range(5):
    dopredu()
    dopredu()
    vpravo()
    vlavo()

end()

screen.mainloop()
