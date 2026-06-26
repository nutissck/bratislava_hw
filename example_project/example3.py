"""
ГРА "Catch the Bubble"
Це навчальна програма на Python з використанням бібліотеки tkinter.
Мета гри — натискати на кульку, яка з’являється у випадковому місці.
Кожне влучання додає 1 бал.
"""
# ===== ІМПОРТ БІБЛІОТЕК =====
from tkinter import *
# Імпортуємо ВСІ класи та функції з бібліотеки tkinter
# tkinter відповідає за вікна, кнопки, написи, canvas
from random import *
# Імпортуємо всі функції з random
# Використовується для випадкових чисел (позиція, розмір, колір)
import time
# Імпортуємо модуль time
# Він дозволяє працювати з часом (таймер гри)

#-------------------ЛОГІКА ГРИ--------------------
# ===== ОСНОВНЕ ТІЛО ПРОГРАМИ - ЗМІННІ ГРИ =====
points = 0
# Змінна для збереження кількості очок
start_time = 0
# Змінна для збереження часу початку гри
running = False
# Логічна змінна
# False — гра не запущена
# True — гра запущена

#------------------ФУНКЦІЇ------------------

# ===== ФУНКЦІЯ СТВОРЕННЯ КУЛЬКИ =====
def spawn_ball():
    # Функція створює нову кульку
    if not running:
        # Якщо гра не запущена
        return
        # Виходимо з функції
    canvas.delete(ALL)
    # Видаляємо попередню кульку
    r = randint(20, 50)
    # Випадковий радіус кульки
    x = randint(r, canvas.winfo_width() - r)
    # Випадкова координата X (щоб кулька не вийшла за межі)
    y = randint(r, canvas.winfo_height() - r)
    # Випадкова координата Y
    color = choice(["aqua", "blue", "fuchsia", "green", "orange", "red"])
    # Випадковий колір кульки
    ball = canvas.create_oval(
        x - r, y - r,
        x + r, y + r,
        fill=color,
        outline=""
    )
    # Малюємо круг (oval) на canvas
    canvas.tag_bind(ball, "<Button-1>", lambda event: hit()) # event - подія
    #canvas.tag_bind(ball, "<Button-1>", hit)  # event - подія
    # Прив’язуємо клік миші до кульки

# ===== ФУНКЦІЯ ВЛУЧАННЯ =====
def hit():
#def hit(event):
    # Функція викликається при кліку на кульку
    global points
    # Доступ до глобальної змінної points
    points += 1
    # Додаємо 1 очко
    points_label.config(text=str(points))
    # Оновлюємо напис з очками
    spawn_ball()
    # Створюємо нову кульку

# ===== ФУНКЦІЯ СТАРТУ ГРИ =====
def start_game():
    # Функція викликається при натисканні кнопки "Старт"
    global points, start_time, running
    # Повідомляємо Python, що будемо змінювати глобальні змінні
    points = 0
    # Обнуляємо кількість очок
    points_label.config(text="0")
    # Оновлюємо напис з очками на екрані
    timer_label.config(text="0 сек")
    # Скидаємо таймер на 0
    start_time = time.time()
    # Записуємо поточний час у секундах
    running = True
    # Вмикаємо режим гри
    spawn_ball()
    # Створюємо першу кульку
    update_timer()
    # Запускаємо таймер
# ===== ФУНКЦІЯ ЗУПИНКИ ГРИ =====
def stop_game():
    # Функція викликається при натисканні кнопки "Стоп"
    global running
    # Доступ до глобальної змінної running
    running = False
    # Вимикаємо гру
    canvas.delete(ALL)
    # Видаляємо всі об’єкти з canvas
# ===== ФУНКЦІЯ ОНОВЛЕННЯ ТАЙМЕРА =====
def update_timer():
    # Функція оновлює таймер кожну секунду
    if running:
        # Перевіряємо, чи гра запущена
        elapsed = int(time.time() - start_time)
        # Обчислюємо, скільки секунд минуло
        timer_label.config(text=f"{elapsed} сек")
        # Оновлюємо напис таймера
        root.after(1000, update_timer)
        # Викликаємо цю ж функцію через 1000 мс (1 сек)

#------------------ІНТЕРФЕЙС-----------------------
root = Tk()
root.title("Catch the Bubble")
# Встановлюємо назву вікна
root.geometry("900x600")

# ===== ЛІВИЙ ФРЕЙМ (ПАНЕЛЬ КЕРУВАННЯ) =====
frame_left = Frame(
    root,          # вказуємо, що фрейм знаходиться всередині root
    bg="#444",     # колір фону фрейму (темно-сірий)
    width=400,     # фіксована ширина фрейму
    height=600,    # фіксована висота фрейму
    padx=10,       # внутрішній відступ зліва і справа
    pady=10        # внутрішній відступ зверху і знизу
)
frame_left.grid(row=0, column=0, sticky="ns")
# Розміщуємо фрейм у таблиці grid
# row=0 — перший рядок
# column=0 — перша колонка (ліва)
# sticky="ns" — фрейм притиснутий до верху і низу

frame_left.grid_propagate(False)
# Забороняємо фрейму змінювати розмір автоматично
# Тепер він завжди має width=400

# ===== ПРАВИЙ ФРЕЙМ (ІГРОВЕ ПОЛЕ) =====
frame_right = Frame(root, bg="white")
# Створюємо правий фрейм з білим фоном
frame_right.grid(row=0, column=1, sticky="nsew")
# Розміщуємо у другій колонці
# sticky="nsew" — розтягується в усі сторони
root.columnconfigure(1, weight=1)
# Дозволяємо другій колонці розтягуватися
root.rowconfigure(0, weight=1)
# Дозволяємо першому рядку розтягуватися
# ===== CANVAS (ПОЛОТНО ДЛЯ МАЛЮВАННЯ) =====
canvas = Canvas(frame_right, bg="white")
# Створюємо Canvas — місце, де будемо малювати кульку
canvas.pack(fill=BOTH, expand=True)
# pack — інший менеджер розміщення
# fill=BOTH — заповнює ширину і висоту
# expand=True — розтягується при зміні вікна


# ===== ЕЛЕМЕНТИ ІНТЕРФЕЙСУ =====
Label(frame_left, text="Очки:", font=("Arial", 12),
      bg="#444", fg="white").pack(anchor="w")
# Напис "Очки"
points_label = Label(frame_left, text="0", font=("Arial", 12),
                     bg="#444", fg="white")
# Напис для показу кількості очок
points_label.pack(anchor="e", pady=(0, 15))
# Розміщуємо напис
Label(frame_left, text="Час:", font=("Arial", 12),
      bg="#444", fg="white").pack(anchor="w")
# Напис "Час"
timer_label = Label(frame_left, text="0 сек", font=("Arial", 12),
                    bg="#444", fg="white")
# Напис для таймера
timer_label.pack(anchor="e", pady=(0, 20))
# Розміщуємо таймер

Button(frame_left, text="Старт", font=("Arial", 12),
       bg="#00cc00", fg="white", command=start_game)\
       .pack(fill=X, pady=5)
# Кнопка запуску гри
Button(frame_left, text="Стоп", font=("Arial", 12),
       bg="#cc0000", fg="white", command=stop_game)\
       .pack(fill=X, pady=5)
# Кнопка зупинки гри




# ===== ЗАПУСК ГОЛОВНОГО ЦИКЛУ =====
root.mainloop()
# Запускаємо програму
# Без цього рядка вікно не з’явиться
