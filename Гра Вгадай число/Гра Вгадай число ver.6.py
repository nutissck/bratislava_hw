from tkinter import *  # Імпортуємо всі компоненти з бібліотеки Tkinter
from random import randint  # Імпортуємо функцію randint для генерації випадкового числа

#ЛОГІКА ПРОГРАМИ
# Глобальні змінні
number = randint(1, 6)  # Випадкове число від 1 до 6 (це число потрібно вгадати)
k = 3  # Початкова кількість спроб
user_wins = 0  # Лічильник перемог користувача
bot_wins = 0  # Лічильник перемог бота
placeholder_text = "Введи число від 1 до 6"  # Текст-заповнювач у полі введення

#Функція перевірки введеного числа
def one_click():
    global k, number, user_wins, bot_wins  # Глобальні змінні
    a = entry.get()  # Отримуємо введене число
    a = int(a)  # Перетворюємо текст у число
    # Перевіряємо, чи число входить у допустимий діапазон
    if a < 1 or a > 6:
        label2.config(text=" Число має бути від 1 до 6!", fg="red")
        entry.delete(0, END)
        return

    k -= 1  # Зменшуємо кількість спроб
    # Перевіряємо, чи користувач вгадав число
    if a < number:
        label2.config(text=f" Залишилось спроб: {k}\nСпробуй більше!", fg="orange")
    elif a > number:
        label2.config(text=f" Залишилось спроб: {k}\nСпробуй менше!", fg="orange")
    else:
        user_wins += 1  # Збільшуємо кількість перемог користувача
        update_score()  # Оновлюємо рахунок
        new_window = Toplevel(root)  # Створюємо нове вікно
        new_window.geometry("350x200")  # Встановлюємо розмір вікна
        new_window.configure(bg="#333333")  # Встановлюємо колір фону
        # Додаємо текстове повідомлення у вікно
        label3 = Label(new_window,
                       text=f"  Вгадав!\nЧисло: {number}\nСпроб залишилось: {k}",
                       font="Arial 16 bold", fg= "lime", bg="#333333")
        label3.pack(pady=20)
        # Кнопка закриття вікна
        close_button = Button(new_window,
                              text="Закрити",
                              font="Arial 12 bold",
                              command=new_window.destroy,
                              bg="red",
                              fg="white",
                              relief=FLAT)
        close_button.pack(pady=10)
        # Відключаємо поле введення та кнопку після завершення гри
        entry.config(state=DISABLED)
        button.config(state=DISABLED)

        return

    # Якщо спроби закінчились – відкриваємо вікно програшу
    if k == 0:
        bot_wins += 1  # Збільшуємо кількість перемог бота
        update_score()  # Оновлюємо рахунок
        new_window = Toplevel(root)  # Створюємо нове вікно
        new_window.geometry("350x200")  # Встановлюємо розмір вікна
        new_window.configure(bg="#333333")  # Встановлюємо колір фону
        # Додаємо текстове повідомлення у вікно
        label3 = Label(new_window,
                       text= f"  Не вгадав!\nЧисло: {number}",
                       font="Arial 16 bold", fg="red", bg="#333333")
        label3.pack(pady=20)
        # Кнопка закриття вікна
        close_button = Button(new_window,
                              text="Закрити",
                              font="Arial 12 bold",
                              command=new_window.destroy,
                              bg="red",
                              fg="white",
                              relief=FLAT)
        close_button.pack(pady=10)
        # Відключаємо поле введення та кнопку після завершення гри
        entry.config(state=DISABLED)
        button.config(state=DISABLED)

    entry.delete(0, END)  # Очищаємо поле введення



#Функція очищує текст у полі введення при фокусі
def on_entry_click(event):
    if entry.get() == placeholder_text:
        entry.delete(0, END)
        entry.config(fg="black")


# Функція для запуску нової гри
def new_game():
    global k, number  # Використовуємо глобальні змінні
    k = 3  # Оновлюємо кількість спроб до 3
    number = randint(1, 6)  # Генеруємо нове випадкове число

    # Очищаємо текст підказок
    label2.config(text=" ", fg="white", bg="#2B2B2B")

    # Активуємо поле введення та кнопку після завершення попередньої гри
    entry.config(state=NORMAL)
    button.config(state=NORMAL)

    # Очищаємо поле введення
    entry.delete(0, END)


def update_score():
    """Оновлює текст із рахунком перемог"""
    score_label.config(text=f"Гравець: {user_wins}  |  Бот: {bot_wins}")


#ІНТЕРФЕЙС ПРОГРАМИ
root = Tk()
root.title("Вгадай число!")  # Назва вікна
root.geometry("500x500")  # Встановлення розміру вікна
root.configure(bg="#2B2B2B")  # Колір фону
root.resizable(False, False)  # Забороняємо зміну розміру вікна

# Лічильник перемог
score_label = Label(root, text=f"Гравець: {user_wins}  |  Бот: {bot_wins}", font="Arial 16 bold", fg="red", bg="#e38a05")
score_label.pack(ipady=10, fill=X)

# Додавання заголовка у вигляді зображення
title_img = PhotoImage(file="image/title.png")
title_label = Label(root, image=title_img, bg="#2B2B2B")
title_label.pack()

# Поле введення для введення числа
entry = Entry(root, font="Arial 10", justify="center", border=3, bg="#FFFFFF", fg="#ff0303")
entry.insert(0, placeholder_text)  # Додаємо текст-заповнювач
entry.bind("<FocusIn>", on_entry_click)  # Очищення тексту при фокусі
entry.place(x=180, y=350, width=150, height=30)
# Кнопка із зображенням кубика
photo = PhotoImage(file="image/cube4.png")
photo = photo.subsample(2, 2)  # Зменшуємо зображення у 2 рази
button = Button(root, image=photo, width=150, height=150, bd=2, command=one_click)
button.place(x=180, y=185)
# Поле для виводу підказок
label2 = Label(root, text=" ", font="Arial 16 bold", fg="#ff0303", bg="#2B2B2B")
label2.place(x=130, y=130)
# Кнопка "NEW GAME" для запуску нової гри
new_game_button = Button(root, text="NEW GAME", font="Arial 14 bold", command=new_game, bd=3, bg="#e38a05", fg="white")
new_game_button.place(x=200, y=460, width=120, height=40)
# Запускаємо головний цикл Tkinter
root.mainloop()
