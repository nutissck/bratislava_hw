from tkinter import *
root = Tk()
root.geometry("400x300")
root.configure(bg="white")
canvas=Canvas(root, width=400, height=300, bg="#ededeb")
canvas.pack()
def stvorec(x,y):
    velkost=100
    medzery=10
    canvas.create_rectangle(
        x, y,
        x + velkost, y + velkost,
        fill='red'
    )
    x2 = x + velkost + medzery
    canvas.create_rectangle(
        x2, y,
        x2 + velkost, y + velkost,
        fill='blue'
    )
    canvas.create_text(
        x+velkost/2,y+velkost/2,
        text='červený', font=('Arial', 20),
        fill="yellow"
    )
    canvas.create_text(
        x2+velkost/2,y+velkost/2,
        text="modry", font=('Arial', 20),
        fill="yellow"
    )

stvorec(50,50)
mainloop()







root.mainloop()
