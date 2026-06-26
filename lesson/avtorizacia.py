from PIL import Image
import customtkinter as ctk
from customtkinter import CTkLabel, CTkEntry

#інтерфейс
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")
root=ctk.CTk()
root.title("Авторизація")
root.geometry("300x300")
root.configure(background="#e3e3e3")

#Логика
correct_login="admin"
correct_password="1234"
img = Image.open("error.png")
error_icon = ctk.CTkImage(light_image=img, size=(60, 60))
img = Image.open("correct.png")
correct_icon = ctk.CTkImage(light_image=img, size=(60, 60))
img = Image.open("znak.png")
znak_icon = ctk.CTkImage(light_image=img, size=(80, 80))
#функція створення вікна результату
def show_result(title,text, color, picture):
    result_window = ctk.CTkToplevel(root)
    result_window.geometry("300x250")
    result_window.title(title)
    result_window.attributes("-topmost", True)

    frame1 = ctk.CTkFrame(result_window, corner_radius=15)
    frame1.pack(pady=30, padx=20, fill="both", expand=True)
    lbl=ctk.CTkLabel(frame1,text=text, text_color=color,font=("Tahoma",25,"bold"))
    lbl.pack(pady=5)
    label_img = ctk.CTkLabel(frame1, image=picture, text="")
    label_img.image = picture
    label_img.pack()
    ctk.CTkButton(frame1, text="Закрити",
    fg_color="#3a485e",
    hover_color="#1c232e",
    text_color="white",
    corner_radius=13,
    height=30,
    width=30,
    font=("Segoe UI", 14, "bold"),
    command=result_window.destroy).pack(pady=10)
#Перевірка логіна та пароля
def check_login():
    login=ent_login.get()
    password=ent_password.get()
    if login=="" or password=="":
        show_result("помилка","Заповніть поля", "#f0cc02", znak_icon)
    elif login==correct_login and password==correct_password:
        show_result("Успіх", "Авторизація\n успішна", "#25b002", correct_icon)
    else:
        show_result("Відмова", "Невірний логін\n або пароль", "#b00202", error_icon)



#інтерфейс
frame = ctk.CTkFrame(root, corner_radius=15)
frame.pack(pady=30, padx=20, fill="both", expand=True)
ctk.CTkLabel(frame,text="Логін", text_color="#2b3545", font=("Tahoma", 18, "bold")).pack()
ent_login=ctk.CTkEntry(frame,  placeholder_text="Введіть логін", text_color="black", width=150 , corner_radius=13)
ent_login.pack(ipady=3)
ctk.CTkLabel(frame,text="Пароль", text_color="#2b3545", font=("Tahoma", 18, "bold")).pack()
ent_password=ctk.CTkEntry(frame, placeholder_text="Введіть пароль", text_color="black", width=150, corner_radius=13)
ent_password.pack(ipady=3)
ctk.CTkButton(frame,
    text="Авторизація",
    fg_color="#3a485e",
    hover_color="#1c232e",
    text_color="white",
    corner_radius=13,
    height=30,
    width=30,
    font=("Segoe UI", 14, "bold"),
    command=check_login).pack(pady=40)

root.mainloop()