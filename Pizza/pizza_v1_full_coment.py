from tkinter.constants import RIGHT, LEFT

import customtkinter as ctk# Імпортуємо бібліотеку tkinter для створення графічного інтерфейсу
from PIL import Image

"""
1. **Імпорт бібліотеки tkinter**:
  - Програма використовує tkinter для створення графічного інтерфейсу користувача.
  - Імпортовано всі компоненти бібліотеки tkinter.
"""


# Функція обчислення ціни піци
"""
2. **Обчислення ціни піци (pizza_price)**:
  - Вартість піци обчислюється на основі обраних користувачем інгредієнтів, розміру та рівня гостроти соусу.
  - Початкова ціна — 20 грн.
  - До ціни додається вартість кожного обраного інгредієнта:
    - Помідори — 10 грн.
    - Сир — 15 грн.
    - Курка — 20 грн.
    - Гриби — 10 грн.
    - Зелень — 5 грн.
  - Залежно від розміру піци:
    - Мала — ціна зменшується на 25%.
    - Велика — ціна збільшується на 25%.
  - Рівень гостроти додає до ціни значення, обране на шкалі.
  - Після обчислення ціна відображається у текстовому полі.
  - Додатково змінюється зображення піци залежно від її розміру.
"""
def pizza_price():
   price = 20  # Стартова вартість піци
   # Додавання вартості залежно від вибраних інгредієнтів
   if taste1.get() == 1:  # Якщо вибрано помідори
       price += 10
   if taste2.get() == 1:  # Якщо вибрано сир
       price += 15
   if taste3.get() == 1:  # Якщо вибрано курку
       price += 20
   if taste4.get() == 1:  # Якщо вибрано гриби
       price += 10
   if taste5.get() == 1:  # Якщо вибрано зелень
       price += 5


   # Регулювання ціни залежно від розміру
   if size.get() == 1:  # Якщо вибрано малу піцу
       price *= 0.75
   elif size.get() == 3:  # Якщо вибрано велику піцу
       price *= 1.25


   # Врахування рівня гостроти через соус
   spice_level = scale.get()  # Отримуємо значення з віджета Scale
   price += spice_level  # Кожен рівень додає до вартості


   # Оновлення тексту ціни
   label_price.configure(text=f"Ціна: {price} грн")  # Відображення обчисленої ціни


   # Зміна зображення піци залежно від розміру
   update_image(size.get())


# Функція оновлення зображення піци
"""
3. **Оновлення зображення піци (update_image)**:
  - Залежно від обраного розміру піци зображення масштабується:
    - Мала — найбільше масштабування.
    - Велика — найменше масштабування.
  - Завантажується файл зображення (`pizza.png`) і змінюється його розмір.
  - Віджет для зображення оновлюється.
"""
def update_image(size):
   # Масштабування зображення залежно від розміру піци
   if size == 1:  # Якщо розмір малий
       scale_factor = 3
   elif size == 2:  # Якщо розмір середній
       scale_factor = 2
   elif size == 3:  # Якщо розмір великий
       scale_factor = 1
   else:  # За замовчуванням (середній розмір)
       scale_factor = 2

   image = Image.open("images/pizza.png")

   pizza_img = ctk.CTkImage(
       light_image=image,
       dark_image=image,
       size=(200, 200)
   )

   pizza_label.configure(image=pizza_img)
   pizza_label.image = pizza_img
   pizza_label.place(relx=0.5, rely=0.5, anchor="center")

# Функція скидання вибору
"""
4. **Скидання вибору (reset_selection)**:
  - Всі опції (інгредієнти, розмір, шкала гостроти) скидаються до початкового стану.
  - Відновлюється початковий текст ціни.
  - Поле зображення очищується.
"""
def reset_selection():
   # Скидання вибору інгредієнтів
   taste1.set(0)
   taste2.set(0)
   taste3.set(0)
   taste4.set(0)
   taste5.set(0)


   # Скидання вибору розміру
   size.set(0)


   # Скидання рівня гостроти
   scale.set(0)


   # Скидання тексту та зображення
   label_price.configure(text="Ціна: 0 грн")
   pizza_label.configure(text="Піца з'явиться тут", image="")


# Налаштування вікна
"""
5. **Налаштування графічного інтерфейсу**:
  - Головне вікно (`root`) налаштоване з розмірами 800x500 пікселів.
  - У лівій частині вікна знаходяться елементи керування:
    - Чекбокси для вибору інгредієнтів.
    - Радіокнопки для вибору розміру.
    - Шкала для налаштування рівня гостроти.
    - Кнопки "Порахувати" та "Скинути".
  - У правій частині вікна відображається зображення піци.
  - Додаткові фрейми використовуються для організації віджетів у структурований спосіб.
"""
root = ctk.CTk()  # Створюємо головне вікно програми
ctk.set_appearance_mode("dark")      # Light, Dark, System
ctk.set_default_color_theme("blue")


# Ліва частина для елементів керування
left_frame = ctk.CTkFrame(root, corner_radius=20)
left_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)


# Права частина для відображення піци
right_frame = ctk.CTkFrame(root, corner_radius=20)
right_frame.pack(side="right", ipadx=100, pady=20, fill="both", expand=True)


# Фрейм для першого стовпчика (інгредієнти)
column1 = ctk.CTkFrame(left_frame, corner_radius=20)  # Створюємо фрейм для інгредієнтів
column1.grid(row=1, column=0, sticky="we", padx=10, pady=20)


# Фрейм для другого стовпчика (розмір піци)
column2 = ctk.CTkFrame(left_frame, corner_radius=20)  # Створюємо фрейм для вибору розміру
column2.grid(row=1, column=1, sticky="we", padx=10)


# Інгредієнти
ingredients_label = ctk.CTkLabel(column1, text="Інгредієнти:", font=("Arial", 16, 'bold'))  # Текстовий напис
ingredients_label.grid(row=0, column=0, sticky="w", pady=(10, 10), padx=(20,10))


# Опції вибору інгредієнтів
taste1 = ctk.IntVar()  # Змінна для зберігання стану
ctk.CTkCheckBox(column1, text="🍅 Помідори",font=("Segoe UI", 14), variable=taste1, onvalue=1, offvalue=0,
    checkbox_height=22,
    checkbox_width=22, fg_color="#fc1d0d",
    hover_color="#f57971").grid(row=1, column=0, sticky='w', pady=(0, 7), padx=(10,10))
taste2 = ctk.IntVar()
ctk.CTkCheckBox(column1, text="🧀 Сир", font=("Segoe UI", 14),variable=taste2, onvalue=1, offvalue=0, checkbox_height=22,
    checkbox_width=22, fg_color="#e0ce07",
    hover_color="#fff47d").grid(row=2, column=0, sticky='w', pady=(0, 7), padx=(10,10))
taste3 = ctk.IntVar()
ctk.CTkCheckBox(column1, text="🍗 Курка",font=("Segoe UI", 14), variable=taste3, onvalue=1, offvalue=0, checkbox_height=22,
    checkbox_width=22, fg_color="#f79d79",
    hover_color="#fcc6b1").grid(row=3, column=0, sticky='w', pady=(0, 7), padx=(10,10))
taste4 = ctk.IntVar()
ctk.CTkCheckBox(column1, text="🍄 Гриби", font=("Segoe UI", 14),variable=taste4, onvalue=1, offvalue=0, checkbox_height=22,
    checkbox_width=22, fg_color="#ad956d",
    hover_color="#c2ac8a").grid(row=4, column=0, sticky='w', pady=(0, 7), padx=(10,10))
taste5 = ctk.IntVar()
ctk.CTkCheckBox(column1, text="🌿 Зелень", font=("Segoe UI", 14), variable=taste5, onvalue=1, offvalue=0, checkbox_height=22,
    checkbox_width=22, fg_color="#07f21f",
    hover_color="#66ff75").grid(row=5, column=0, sticky='w', pady=(0, 7), padx=(10,10))


# Розмір піци
size_label = ctk.CTkLabel(column2, text="Розмір піци:", font=("Arial", 16, 'bold'))  # Текстовий напис
size_label.grid(row=0, column=0, sticky='w',  pady=(10, 10), padx=(20,10))


size = ctk.IntVar()  # Змінна для зберігання вибору розміру
ctk.CTkRadioButton(column2, text="Мала", variable=size, value=1, font=("Segoe UI", 14),
    corner_radius=10, radiobutton_width=20,
    radiobutton_height=20,
    fg_color="#fcfbfa",
    hover_color="#d9d9d9").grid(row=1, column=0, sticky='w', pady=(0, 7), padx=(10,10))
ctk.CTkRadioButton(column2, text="Середня", variable=size, value=2, font=("Segoe UI", 14),
    corner_radius=10, radiobutton_width=20,
    radiobutton_height=20,
    fg_color="#fcfbfa",
    hover_color="#d9d9d9").grid(row=2, column=0, sticky='w', pady=(0, 7), padx=(10,10))
ctk.CTkRadioButton(column2, text="Велика", variable=size, value=3, font=("Segoe UI", 14),
    corner_radius=10, radiobutton_width=20,
    radiobutton_height=20,
    fg_color="#fcfbfa",
    hover_color="#d9d9d9").grid(row=3, column=0, sticky='w', pady=(0, 7), padx=(10,10))

# Шкала для вибору соусу
scale_label = ctk.CTkLabel(left_frame, text="🌶 Гострота соусу", font=("Arial", 14))  # Текстовий напис
scale_label.grid(row=2, column=0, columnspan=2, pady=(0, 0))

scale = ctk.CTkSlider(left_frame,from_=0,to=5,number_of_steps=5, width=300,corner_radius=10,button_color="#d9d8d7",
        progress_color="#a6a5a4",
        button_hover_color="#969696")
scale.grid(row=3, column=0, columnspan=2, pady=5)


# Кнопки
button_frame = ctk.CTkFrame(left_frame, corner_radius=20)  # Фрейм для кнопок
button_frame.grid(row=4, column=0, columnspan=2, pady=10, padx=10)


ctk.CTkButton(button_frame, text="Порахувати", font=("Arial", 14), command=pizza_price,
    width=180,
    height=40,
    corner_radius=15,fg_color="#8a8988", hover_color="#70706f").pack(side="left", padx=5)  # Кнопка обчислення
ctk.CTkButton(button_frame, text="Скинути", font=("Arial", 14), command=reset_selection, width=180,
    height=40,
    corner_radius=15, fg_color="#8a8988", hover_color="#70706f").pack(side="right", padx=5)# Кнопка скидання


# Виведення ціни
label_price = ctk.CTkLabel(left_frame, text="Ціна: 0 грн", font=("Arial", 16, "bold"))  # Текстовий напис
label_price.grid(row=5, column=0, columnspan=2, pady=10)


# Відображення піци
pizza_label = ctk.CTkLabel(right_frame, text="Піца з'явиться тут")  # Поле для зображення піци
pizza_label.pack()


#ВАЖЛИВО

# Налаштування стовпців у головному вікні
root.columnconfigure(0, weight=1)  # Ліва частина
root.columnconfigure(1, weight=3)  # Права частина

# Налаштування стовпців у лівій частині (left_frame)
left_frame.columnconfigure(0, weight=1)
left_frame.columnconfigure(1, weight=1)




# Запуск програми
"""
6. **Запуск програми**:
  - Основний цикл програми (`root.mainloop()`) забезпечує взаємодію з користувачем та оновлення інтерфейсу.
"""
root.mainloop()  # Запускаємо графічний інтерфейс
