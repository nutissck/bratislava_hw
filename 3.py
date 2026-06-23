from tkinter import *
root = Tk()
root.geometry("500x400")
canvas = Canvas(root, width=500, height=400, bg="#ededeb")
canvas.pack()
def dva_stvorce(x,y,a1,a2):
    canvas.create_rectangle(
        x, y, x+a1, y+a1,
        fill="indian red"
    )
    cx=x+a1/2
    cy=y+a1/2
    canvas.create_rectangle(
        cx-a2/2, cy-a2/2, cx + a2/2, cy+a2/2,
        fill="light blue"
    )
    canvas.create_text(
        x-10, y-5, text="A", font=('Arial', 15),
    )
    canvas.create_text(
        (x+a1)+10, y-5, text="B", font=('Arial', 15),
    )
    canvas.create_text(
        (x+a1)+10, (y+a1)+5, text="C", font=('Arial', 15),
    )
    canvas.create_text(
        x-10,(y+a1)+5, text="D", font=('Arial', 15),
    )
    canvas.create_text(
        (x+a1)+20, cy, text=str(a1), font=('Arial', 12),
    )
    canvas.create_text(
        cx, (cy+a2/2)-10,
        text=str(a2), font=('Arial', 12),
    )
dva_stvorce(50,50,180,100)
root.mainloop()