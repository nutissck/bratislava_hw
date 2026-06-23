from tkinter import *
root = Tk()
root.geometry("500x400")
canvas = Canvas(root, width=500, height=400, bg="#ededeb")
canvas.pack()
def vlajky():
    w=135
    h=90
    gap=20
    #GERMANY
    x = 20
    y = 20
    canvas.create_rectangle(x, y, x + w, y + h, outline='black', width=2)

    canvas.create_rectangle(x, y, x+w, y+h/3, fill='black', width=0)
    canvas.create_rectangle(x, y+h/3, x+w, y+2*h/3, fill='red', width=0)
    canvas.create_rectangle(x, y+2*h/3, x+w, y+h, fill='gold', width=0)
    #ITALY
    x=x+w+gap
    canvas.create_rectangle(x, y, x + w, y + h, outline='black', width=2)

    canvas.create_rectangle(x, y, x+w/3,y+h, fill='green', width=0)
    canvas.create_rectangle(x+w/3, y,  x+2*w/3, y+h, fill='white', width=0)
    canvas.create_rectangle(x+2*w/3, y, x+w, y+h, fill='red', width=0)
    #FRANCE
    y=y+h+gap
    x=20
    canvas.create_rectangle(x, y, x + w, y + h, outline='black', width=2)

    canvas.create_rectangle(x, y, x + w / 3, y + h, fill='blue', width=0)
    canvas.create_rectangle(x + w / 3, y, x + 2 * w / 3, y + h, fill='white', width=0)
    canvas.create_rectangle(x + 2 * w / 3, y, x + w, y + h, fill='red', width=0)
    #UKRAIN
    y=20+h+gap
    x=20+w+gap
    canvas.create_rectangle(x, y, x + w, y + h, outline='black', width=2)

    canvas.create_rectangle(x, y, x + w, y + h / 2, fill='blue', width=0)
    canvas.create_rectangle(x, y + h / 2, x + w, y + h, fill='yellow', width=0)
vlajky()
root.mainloop()