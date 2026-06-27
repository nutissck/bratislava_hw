from tkinter import *
#logika
def paint(event):
    x1=event.x-10
    y1=event.y-10
    x2=event.x+10
    y2=event.y+10
    c.create_oval(x1,y1,x2,y2,fill="red", outline="")
def clear(event=None):
    c.delete("all")

#interface
root=Tk()
c=Canvas(root,width=600,height=600)
c.pack()

c.bind("<B1-Motion>", paint)#утримуємо ліву кнопку миші
"""b=Button(root,text="Clear", command=clear)
b.pack()"""
b=Button(root,text="Clear")
b.pack()
b.bind("<Button-3>", clear)
root.mainloop()
