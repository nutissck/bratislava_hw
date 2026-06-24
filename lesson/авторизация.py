from tkinter import *
#інтерфейс
root=Tk()
root.title("Авторизація")
root.geometry("300x300")
root.configure(background="#e3e3e3")

#Логика
correct_login="admin"
correct_password="1234"
#функція створення вікна результату
def show_result(title,text, color):
    result_window = Toplevel(root)
    result_window.geometry("300x150")
    result_window.title(title)
    result_window.configure(background="#ededeb")
    lbl=Label(result_window,text=text,bg="#ededeb", fg=color,font=("Arial",20,"bold"))
    lbl.pack()
    Button(result_window, text="Закрити", command=result_window.destroy, bg="#908d96").pack()
#Перевірка логіна та пароля
def check_login():
    login=ent_login.get()
    password=ent_password.get()
    if login=="" or password=="":
        show_result("помилка","Заповніть поля", "orange")
    elif login==correct_login and password==correct_password:
        show_result("Успіх", "Авторизація успішна", "green")
    else:
        show_result("Відмова", "Невірний логін або пароль", "red")



#інтерфейс
Label(root,text="Логін",bg="#e3e3e3", fg="black", font=("Arial", 20)).pack()
ent_login=Entry(root,bg="white", border=5, fg="black", width=30 )
ent_login.pack(ipady=5)
Label(root,text="Пароль",bg="#e3e3e3", fg="black", font=("Arial", 20)).pack()
ent_password=Entry(root,bg="white", border=5, fg="black", width=30 )
ent_password.pack(ipady=5)
Button(root, text="Авторизація",bg="#908d96", font=("Arial", 12), command=check_login).pack(pady=10)

root.mainloop()