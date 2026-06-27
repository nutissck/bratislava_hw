from tkinter import *  # Підключаємо модуль tkinter

root = Tk()  # Створення головного вікна
root.title("Форма авторизації")  # Назва вікна
root.geometry("400x400")  # Розмір вікна
root.configure(bg="#f0f0f0")  # Фон вікна

# Додаємо функцію
def btn_click():
    lblrezult1.config(text=f"Клієнт {ent1.get()} авторизований\nЛогін: {ent1.get()}\nПароль: {ent2.get()}")
    ent1.delete(0, END)  # Очищення текстового поля логіна
    ent2.delete(0, END)  # Очищення текстового поля пароля

# Створюємо рамку для форми
frame = Frame(root, bg="#ffffff", padx=20, pady=20, relief=RIDGE, borderwidth=5)
frame.pack(pady=50)

# Додаємо віджет - мітка для логіна
lbl1 = Label(frame, text="Логін", font=("Arial", 12), bg="#ffffff")
lbl1.grid(row=0, column=0, pady=5, padx=10, sticky=W)

# Додаємо віджет - текстове поле для логіна
ent1 = Entry(frame, border=3,  show="*", bg="#e0ffe0", font=("Arial", 12))
ent1.grid(row=0, column=1, pady=5, padx=10)

# Додаємо віджет - мітка для пароля
lbl2 = Label(frame, text="Пароль", font=("Arial", 12), bg="#ffffff")
lbl2.grid(row=1, column=0, pady=5, padx=10, sticky=W)

# Додаємо віджет - текстове поле для пароля
ent2 = Entry(frame, border=3, show="*", bg="#ffe0e0", font=("Arial", 12))
ent2.grid(row=1, column=1, pady=5, padx=10)

# Додаємо віджет - кнопка
btn = Button(frame, text="Вхід в акаунт", command=btn_click, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
btn.grid(row=2, columnspan=2, pady=10)

# Додаємо віджет - мітка для результату
lblrezult1 = Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
lblrezult1.pack()

root.mainloop()

