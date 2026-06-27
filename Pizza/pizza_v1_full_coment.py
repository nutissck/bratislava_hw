from tkinter import *  # Імпортуємо бібліотеку tkinter для створення графічного інтерфейсу


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


   pizza_img = PhotoImage(file="images\pizza.png")  # Завантажуємо зображення піци
   resized_img = pizza_img.subsample(scale_factor, scale_factor)  # Масштабуємо зображення
   pizza_label.configure(image=resized_img)  # Оновлюємо зображення у віджеті
   pizza_label.image = resized_img  # Зберігаємо посилання на зображення (щоб його не видалило)


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
root = Tk()  # Створюємо головне вікно програми
root.title("Піцерія")  # Встановлюємо заголовок вікна
root.geometry("800x500")  # Встановлюємо розміри вікна
root.configure(padx=10, pady=10)  # Додаємо відступи


# Ліва частина для елементів керування
left_frame = Frame(root)  # Створюємо фрейм для керування
left_frame.grid(row=0, column=0, sticky=N, padx=10, pady=10)


# Права частина для відображення піци
right_frame = Frame(root)  # Створюємо фрейм для відображення піци
right_frame.grid(row=0, column=1, sticky=N, padx=10, pady=10)


# Фрейм для першого стовпчика (інгредієнти)
column1 = Frame(left_frame)  # Створюємо фрейм для інгредієнтів
column1.grid(row=1, column=0, sticky=W, padx=10)


# Фрейм для другого стовпчика (розмір піци)
column2 = Frame(left_frame)  # Створюємо фрейм для вибору розміру
column2.grid(row=1, column=1, sticky=W, padx=10)


# Інгредієнти
ingredients_label = Label(column1, text="Інгредієнти:", font=("Arial", 14))  # Текстовий напис
ingredients_label.grid(row=0, column=0, sticky=W, pady=(45, 0))


# Опції вибору інгредієнтів
taste1 = IntVar()  # Змінна для зберігання стану
Checkbutton(column1, text="Помідори", variable=taste1, onvalue=1, offvalue=0).grid(row=1, column=0, sticky=W)
taste2 = IntVar()
Checkbutton(column1, text="Сир", variable=taste2, onvalue=1, offvalue=0).grid(row=2, column=0, sticky=W)
taste3 = IntVar()
Checkbutton(column1, text="Курка", variable=taste3, onvalue=1, offvalue=0).grid(row=3, column=0, sticky=W)
taste4 = IntVar()
Checkbutton(column1, text="Гриби", variable=taste4, onvalue=1, offvalue=0).grid(row=4, column=0, sticky=W)
taste5 = IntVar()
Checkbutton(column1, text="Зелень", variable=taste5, onvalue=1, offvalue=0).grid(row=5, column=0, sticky=W)


# Розмір піци
size_label = Label(column2, text="Розмір піци:", font=("Arial", 14))  # Текстовий напис
size_label.grid(row=0, column=0, sticky=W, pady=5)


size = IntVar()  # Змінна для зберігання вибору розміру
Radiobutton(column2, text="Мала", variable=size, value=1).grid(row=1, column=0, sticky=W)
Radiobutton(column2, text="Середня", variable=size, value=2).grid(row=2, column=0, sticky=W)
Radiobutton(column2, text="Велика", variable=size, value=3).grid(row=3, column=0, sticky=W)


# Шкала для вибору соусу
scale_label = Label(left_frame, text="Соус", font=("Arial", 14))  # Текстовий напис
scale_label.grid(row=2, column=0, columnspan=2, pady=(20, 0))


scale = Scale(left_frame, from_=0, to=5, orient=HORIZONTAL, length=300)  # Шкала для вибору
scale.grid(row=3, column=0, columnspan=2, pady=5)


# Кнопки
button_frame = Frame(left_frame)  # Фрейм для кнопок
button_frame.grid(row=4, column=0, columnspan=2, pady=10)


Button(button_frame, text="Порахувати", command=pizza_price, font=("Arial", 14)).pack(side=LEFT, padx=5)  # Кнопка обчислення
Button(button_frame, text="Скинути", command=reset_selection, font=("Arial", 14)).pack(side=RIGHT, padx=5)  # Кнопка скидання


# Виведення ціни
label_price = Label(left_frame, text="Ціна: 0 грн", font=("Arial", 16, "bold"))  # Текстовий напис
label_price.grid(row=5, column=0, columnspan=2, pady=10)


# Відображення піци
pizza_label = Label(right_frame, text="Піца з'явиться тут")  # Поле для зображення піци
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
