from tkinter import *  # Імпортуємо всі компоненти з модуля tkinter для створення графічного інтерфейсу
from random import randint, choice  # Імпортуємо функції для генерації випадкових чисел і вибору випадкового елемента

# Створення головного вікна та полотна

# Створюємо головне вікно
tk = Tk()
# Створюємо полотно з розмірами 650x800 пікселів
canvas = Canvas(tk, width=650, height=800)
# Додаємо полотно до вікна
canvas.pack()

# -------------------- Створення дороги --------------------

# Створюємо верхню частину дороги сірого кольору
road1 = canvas.create_rectangle(80, 0, 560, 800, fill="gray")
# Створюємо нижню частину дороги для ефекту безкінечного руху
road2 = canvas.create_rectangle(80, -800, 560, 0, fill="gray")
# Створюємо білу роздільну лінію по центру дороги (верхня частина)
center_line1 = canvas.create_line(320, 0, 320, 800, fill="white", dash=(15, 23))
# Створюємо білу роздільну лінію по центру дороги (нижня частина)
center_line2 = canvas.create_line(320, -800, 320, 0, fill="white", dash=(15, 23))

# -------------------- Завантаження зображень --------------------

# Список зображень машин, що їдуть вниз
car_down_images = [
    PhotoImage(file="image/car_down1.png"),
    PhotoImage(file="image/car_down2.png"),
    PhotoImage(file="image/car_down3.png")
]

# Список зображень машин, що їдуть вгору
car_up_images = [
    PhotoImage(file="image/car_up1.png"),
    PhotoImage(file="image/car_up2.png")
]

# Зображення машини гравця
player_car_image = PhotoImage(file="image/player_car.png")

# -------------------- Авто гравця --------------------

# Додаємо зображення машини гравця на координати (500, 170)
player_car = canvas.create_image(500, 170, anchor=NW, image=player_car_image)
# Початкова горизонтальна швидкість
player_x_speed = 0
# Початкова вертикальна швидкість (імітація руху вперед)
player_y_speed = 3
# Максимальна дозволена швидкість
player_max_speed = 10
# Мінімальна дозволена швидкість
player_min_speed = 1

# -------------------- Функції керування гравцем --------------------

# Рух гравця по горизонталі та обмеження в межах дороги

def move_player():
    global player_x_speed
    canvas.move(player_car, player_x_speed, 0)  # Рухаємо по X
    pos = canvas.coords(player_car)  # Отримуємо координати
    if pos[0] < 80:  # Якщо вийшли за ліву межу дороги
        canvas.move(player_car, 80 - pos[0], 0)
    elif pos[0] + player_car_image.width() > 560:  # Якщо вийшли за праву межу дороги
        canvas.move(player_car, 560 - (pos[0] + player_car_image.width()), 0)

# Прискорення гравця

def accelerate():
    global player_y_speed
    if player_y_speed < player_max_speed:
        player_y_speed += 1

# Гальмування гравця

def brake():
    global player_y_speed
    if player_y_speed > player_min_speed:
        player_y_speed -= 1

# Обробка натискання клавіш

def key_pressed(event):
    global player_x_speed
    if event.keysym == "Left":
        player_x_speed = -5
    elif event.keysym == "Right":
        player_x_speed = 5
    elif event.keysym == "Up":
        accelerate()
    elif event.keysym == "Down":
        brake()

# Обробка відпускання клавіш

def key_released(event):
    global player_x_speed
    if event.keysym in ("Left", "Right"):
        player_x_speed = 0


# -------------------- Створення інших авто --------------------

# Список інших автомобілів на дорозі
other_cars = []
# Мінімальна відстань між машинами по X
min_distance_x = 60

# Створення нової машини на полотні

def create_car(x, y, image, direction):
    # Створюємо зображення машини на вказаних координатах x та y з заданим зображенням
    car_id = canvas.create_image(x, y, anchor=NW, image=image)
    # Генеруємо випадкову швидкість руху для машини (від 2 до 5 пікселів за кадр)
    speed = randint(2, 5)
    # Додаємо машину до списку керованих об'єктів з напрямком руху та швидкістю
    # direction — це напрямок руху машини: "up" означає рух вгору, "down" — вниз
    other_cars.append((car_id, direction, speed))  # (car_id, direction, speed) це кортеж який має індекс і



# Перевірка на достатню відстань між авто при генерації
def check_x_collision(x, min_distance):
    # Перевіряємо, чи є на цій координаті X вже інша машина занадто близько
    for car in other_cars:
        car_pos = canvas.coords(car[0])  # Отримуємо координати існуючої машини
        if abs(x - car_pos[0]) < min_distance:  # Якщо відстань по X менше, ніж дозволено
            return True  # Повертаємо True — колізія
    return False  # Інакше повертаємо False — розміщення дозволене


# Створюємо 2 авто, що їдуть вниз
for _ in range(2):  # Цикл повторюється 2 рази для створення двох машин
    img = choice(car_down_images)  # Випадковим чином обираємо зображення з машинами, що рухаються вниз
    x = randint(100, 240)  # Генеруємо випадкову координату X в межах лівої половини дороги
    while check_x_collision(x, min_distance_x):  # Перевіряємо, чи на цій координаті вже є машина занадто близько
        x = randint(100, 240)  # Якщо є, генеруємо нову координату X, доки не знайдемо безпечну
    y = randint(-800, -100)  # Генеруємо випадкову координату Y — початкова позиція поза екраном (зверху)
    create_car(x, y, img, "down")  # Створюємо машину з напрямком руху вниз

# Створюємо 2 авто, що їдуть вгору
for _ in range(2):  # Цикл повторюється 2 рази для створення двох машин
    img = choice(car_up_images)  # Випадковим чином обираємо зображення з машинами, що рухаються вгору
    x = randint(360, 480)  # Генеруємо випадкову координату X в межах правої половини дороги
    while check_x_collision(x, min_distance_x):  # Перевіряємо, чи є інша машина надто близько по X
        x = randint(360, 480)  # Якщо є, генеруємо нову координату X
    y = randint(900, 1500)  # Генеруємо координату Y — старт за межами екрана (знизу)
    create_car(x, y, img, "up")  # Створюємо машину з напрямком руху вгору



# Рух інших машин

def move_other_cars():
    # Проходимо по кожному елементу списку other_cars за індексом
    for i in range(len(other_cars)):
        # Розпаковуємо кортеж: отримуємо ID машини, напрямок руху ("up"/"down") та швидкість
        car_id, direction, speed = other_cars[i]
        # Отримуємо поточні координати машини на полотні
        pos = canvas.coords(car_id)
        if direction == "down":  # Якщо машина рухається вниз
            canvas.move(car_id, 0, speed)  # Зсуваємо її вниз по Y на значення швидкості
            if pos[1] > 800:  # Якщо машина вийшла за нижню межу екрану
                canvas.move(car_id, 0, -900)  # Повертаємо її назад угору, за межі вікна
        else:  # Якщо машина рухається вгору
            canvas.move(car_id, 0, -speed)  # Зсуваємо її вгору по Y на значення швидкості
            if pos[1] < -80:  # Якщо машина вийшла за верхню межу екрану
                canvas.move(car_id, 0, 900)  # Повертаємо її вниз, за межі екрана


# Перевірка зіткнення машини гравця з іншими авто

def check_collision():
    # Отримуємо координати машини гравця
    player_pos = canvas.coords(player_car)

    # Проходимо по кожному авто на дорозі
    # Розпаковуємо кортеж із трьох значень: (car_id, direction, speed)
    # Нам потрібен лише car_id, а direction і speed — ігноруємо, тому використовуємо "_" як заглушки
    for car_id, _, _ in other_cars:
        # Отримуємо координати поточної машини
        car_pos = canvas.coords(car_id)

        # Перевіряємо чи машини досить близько одна до одної по X та Y — якщо так, вважаємо це зіткненням
        if abs(player_pos[0] - car_pos[0]) < 50 and abs(player_pos[1] - car_pos[1]) < 50:
            return True  # Зіткнення виявлено

    return False  # Зіткнення не виявлено


# -------------------- Анімація гри --------------------

# Основна функція циклу гри

def animate():
    if check_collision():
        # Виводимо текст при аварії
        canvas.create_text(325, 400, text="Аварія! Виклик поліції!", font=("Arial", 30), fill="red")
        return

    # Рух дороги вниз (імітація руху вперед)
    canvas.move(road1, 0, player_y_speed)
    canvas.move(road2, 0, player_y_speed)
    canvas.move(center_line1, 0, player_y_speed)
    canvas.move(center_line2, 0, player_y_speed)

    # Повертаємо частини дороги нагору при досягненні нижньої межі
    if canvas.coords(road1)[1] >= 800:
        canvas.move(road1, 0, -1600)
        canvas.move(center_line1, 0, -1600)
    if canvas.coords(road2)[1] >= 800:
        canvas.move(road2, 0, -1600)
        canvas.move(center_line2, 0, -1600)

    move_player()  # Рух гравця
    move_other_cars()  # Рух інших авто
    tk.after(20, animate)  # Повтор анімації кожні 20 мс


# -------------------- Запуск гри --------------------

# Прив'язка обробки натискання клавіш
tk.bind("<KeyPress>", key_pressed)
# Прив'язка обробки відпускання клавіш
tk.bind("<KeyRelease>", key_released)

# Запускаємо основну анімацію
animate()

# Запускаємо цикл обробки подій Tkinter
tk.mainloop()
