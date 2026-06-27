#event_key_example_1
from tkinter import *
#logika
def up(event):
    c.move(a, 0,-5)
def down(event):
    c.move(a, 0,5)
def left(event):
    c.move(a, -5,0)
def right(event):
    c.move(a, 5,0)

#interface
root = Tk()
root.geometry("400x400")
c=Canvas(root,width=400,height=400)
c.pack()
a=c.create_rectangle(50,50,100,100,fill="red")
c.focus_set()#focus na Canvas, щоб була реакція на клавіші
c.bind("<Up>", up)#bind-зв'язуе натискання клавіши і вклик функції
c.bind("<Down>", down)
c.bind("<Left>", left)
c.bind("<Right>", right)



root.mainloop()
