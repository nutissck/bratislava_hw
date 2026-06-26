from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageGrab

# Глобальні змінні
current_color = "red"
brush_size = 1

# Функція для малювання
def paint(event):
    x1, y1 = event.x - brush_size, event.y - brush_size
    x2, y2 = event.x + brush_size, event.y + brush_size
    canv.create_oval(x1, y1, x2, y2, fill=current_color, outline="")

# Функція для відкриття зображення
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((canv.winfo_width(), canv.winfo_height()), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        canv.create_image(0, 0, anchor=NW, image=img_tk)
        canv.image = img_tk  # Збереження посилання для уникнення видалення

# Функції для зміни кольору
def set_color(color):
    global current_color
    current_color = color

# Функція для зміни розміру пензлика
def set_brush_size(val):
    global brush_size
    brush_size = int(val)

# Функція для очищення полотна
def clear():
    canv.delete("all")

# Функція для збереження полотна
def save():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
    if file_path:
        root.update()
        x = root.winfo_rootx() + canv.winfo_x()
        y = root.winfo_rooty() + canv.winfo_y()
        x1 = x + canv.winfo_width()
        y1 = y + canv.winfo_height()
        img = ImageGrab.grab((x, y, x1, y1))
        img.save(file_path)

# Інтерфейс головного вікна
root = Tk()
root.title("Paint")

# Фрейм для полотна
frame_left = Frame(root)
frame_left.grid(row=0, column=0, sticky="nsew")

# Фрейм для панелі інструментів
frame_right = Frame(root)
frame_right.grid(row=0, column=1, sticky="ns")

# Полотно для малювання
canv = Canvas(frame_left, bg="white", width=500, height=500)
canv.grid(row=0, column=0, sticky="nsew")
canv.bind("<B1-Motion>", paint)

# Кнопки кольорів
colors = ["red", "green", "blue", "white", "black"]
for i, color in enumerate(colors):
    Button(frame_right, bg=color, width=4, height=2, command=lambda c=color: set_color(c)).grid(row=i, column=0, pady=2)

# Шкала для регулювання розміру пензлика
scale = Scale(frame_right, from_=1, to=20, orient=HORIZONTAL, label="Розмір", command=set_brush_size)
scale.grid(row=len(colors), column=0, pady=10)
scale.set(1)

# Кнопки дій
Button(frame_right, text="Очистити", font="Arial 12", bg="#0000ff", fg="white", command=clear).grid(row=len(colors)+1, column=0, pady=5)
Button(frame_right, text="Зберегти", font="Arial 12", bg="#00aa00", fg="white", command=save).grid(row=len(colors)+2, column=0, pady=5)
Button(frame_right, text="Відкрити", font="Arial 12", bg="#ffaa00", fg="black", command=open_image).grid(row=len(colors)+3, column=0, pady=5)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=5)
root.columnconfigure(1, weight=1)
frame_left.rowconfigure(0, weight=1)
frame_left.columnconfigure(0, weight=1)

root.mainloop()
