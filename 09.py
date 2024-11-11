import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    password_characters = []
    if lowercase_var.get():
        password_characters.extend(string.ascii_lowercase)
    if digits_var.get():
        password_characters.extend(string.digits)
    if special_chars_var.get():
        password_characters.extend("!@#$%")
    if not password_characters:
        password_label.config(text="Пожалуйста, выберите хотя бы один тип символов")
        return
    password = ''.join(random.choice(password_characters) for _ in range(password_length))
    password_label.config(text=password)

window = tk.Tk()
window.title("Генератор паролей")

length_label = tk.Label(window, text="Длина пароля:")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1)
length_entry.insert(0, "12")

lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(window, text="Нижний регистр", variable=lowercase_var)
lowercase_check.grid(row=1, columnspan=2)

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(window, text="Цифры", variable=digits_var)
digits_check.grid(row=2, columnspan=2)

special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(window, text="Спецсимволы", variable=special_chars_var)
special_chars_check.grid(row=3, columnspan=2)

generate_button = tk.Button(window, text="Сгенерировать", command=generate_password)
generate_button.grid(row=4, columnspan=2)

password_label = tk.Label(window, text="")
password_label.grid(row=5, columnspan=2)

window.mainloop()
