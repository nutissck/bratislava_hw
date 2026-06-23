from tkinter import *
from random import randint
root = Tk()
root.geometry("500x400")
canvas = Canvas(root, width=500, height=400, bg="navy")
canvas.pack()
def hviezda(n):
    for i in range(n):
        x=randint(0,500)
        y=randint(0,400)
        velkost=randint(10,20)
        canvas.create_text(
        x, y, text="*", fill="yellow", font=f"Arial {velkost}",
    )
hviezda(200)
root.mainloop()