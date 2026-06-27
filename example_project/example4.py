from tkinter import *
from random import *


def create_bubble(count):
    global x, y, r  # Глобальні змінні для координат і радіусу бульбашки
    if count > 0:  # Перевірка, чи є ще необхідна кількість бульбашок для створення
        colors = choice(["aqua", "blue", "fuchsia", "green", "maroon", "orange"])  # Випадковий вибір кольору
        x = randint(0, 500)  # Випадкове горизонтальне положення
        y = randint(0, 500)  # Випадкове вертикальне положення
        r = randint(10, int(50 / 5))  # Випадковий радіус
        # Створення бульбашки
        c.create_oval(x - r, y - r, x + r, y + r, fill=colors)
        # Виклик функції затримки для створення наступної бульбашки
        root.after(1500, create_bubble, count - 1)


def up(event):
    c.move(a, 0, -5)  # Перемістити прямокутник вгору на 5 пікселів при натисканні на стрілку вгору
    check_collision()


def down(event):
    c.move(a, 0, 5)  # Перемістити прямокутник вниз на 5 пікселів при натисканні на стрілку вниз
    check_collision()


def left(event):
    c.move(a, -5, 0)  # Перемістити прямокутник вліво на 5 пікселів при натисканні на стрілку вліво
    check_collision()


def right(event):
    c.move(a, 5, 0)  # Перемістити прямокутник вправо на 5 пікселів при натисканні на стрілку вправо
    check_collision()


def check_collision():
    global x, y, r
    square_coords = c.coords(a)
    square_x = (square_coords[0] + square_coords[2]) / 2  # Центр квадрата за координатою x
    square_y = (square_coords[1] + square_coords[3]) / 2  # Центр квадрата за координатою y

    # Перевіряємо кожен круг на перетин з квадратом
    for item in c.find_all():
        if item != a:  # Якщо об'єкт не є квадратом
            coords = c.coords(item)
            circle_x = (coords[0] + coords[2]) / 2  # Центр круга за координатою x
            circle_y = (coords[1] + coords[3]) / 2  # Центр круга за координатою y

            # Якщо квадрат наближається до круга, то видаляємо круг
            if abs(square_x - circle_x) < r + (coords[2] - coords[0]) / 2 and abs(square_y - circle_y) < r + (
                    coords[3] - coords[1]) / 2:
                c.delete(item)


def clear():
    c.delete("all")  # Видаляє всі об'єкти


root = Tk()
root.title("Спіймай бульбашку")

# Створення полотна для відображення бульбашок
c = Canvas(root, width=500, height=500)
c.pack()
a = c.create_rectangle(50, 50, 100, 100, fill="green")  # Малюємо прямокутник на полотні

# основна програма
create_bubble(100)  # Виклик функції для створення бульбашок

# Створення кнопки "Нова гра"
but = Button(root, text="New Game", font="Arial 12", bg="#0000ff", command=clear)
but.pack()

c.focus_set()  # Встановлюємо фокус на Canvas, щоб він міг реагувати на клавіші
c.bind("<Up>", up)  # Зв'язуємо натискання стрілки вгору з функцією on_up_arrow
c.bind("<Down>", down)  # Зв'язуємо натискання стрілки вниз з функцією on_down_arrow
c.bind("<Left>", left)  # Зв'язуємо натискання стрілки вліво з функцією on_left_arrow
c.bind("<Right>", right)  # Зв'язуємо натискання стрілки вправо з функцією on_right_arrow

root.mainloop()  # Запускаємо головний цикл програми



