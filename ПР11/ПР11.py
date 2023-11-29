from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton
from tkinter import messagebox
from tkinter import Menu
from tkinter import filedialog
from tkinter import scrolledtext


import tkinter as tk
from tkinter import messagebox, filedialog

# Функция обработки нажатия кнопки
def show_message():
    text = ""
    if var1.get():
        text += "Вы выбрали первый вариант.\n"
    if var2.get():
        text += "Вы выбрали второй вариант.\n"
    if var3.get():
        text += "Вы выбрали третий вариант.\n"
    messagebox.showinfo("Выбор", text)

# Функция загрузки текста из файла
def load_file():
    file_path = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
        text_entry.delete("1.0", tk.END)
        text_entry.insert(tk.END, text)

# Создание главного окна
root = tk.Tk()
root.title("Гусев Владимир Иванович")

# Создание вкладок
tab_control = tk.ttk.Notebook(root)
tab1 = tk.Frame(tab_control)
tab2 = tk.Frame(tab_control)
tab3 = tk.Frame(tab_control)
tab_control.add(tab1, text="Калькулятор")
tab_control.add(tab2, text="Чекбоксы")
tab_control.add(tab3, text="Работа с текстом")
tab_control.pack(expand=1, fill="both")

# Вкладка "Калькулятор"
number1_label = tk.Label(tab1, text="Первое число:")
number1_label.pack()
number1_entry = tk.Entry(tab1)
number1_entry.pack()

number2_label = tk.Label(tab1, text="Второе число:")
number2_label.pack()
number2_entry = tk.Entry(tab1)
number2_entry.pack()

operation_label = tk.Label(tab1, text="Операция:")
operation_label.pack()
operation_combobox = tk.ttk.Combobox(tab1, values=["+", "-", "*", "/"])
operation_combobox.pack()



result_label = tk.Label(tab1)
result_label.pack()

def calculate():
    try:
        num1 = float(number1_entry.get())
        num2 = float(number2_entry.get())
        operation = operation_combobox.get()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        
        result_label.config(text="Результат: {}".format(result))
    except ValueError:
        result_label.config(text="Ошибка: неверные значения")

calculate_button = tk.Button(tab1, text="Вычислить", command=calculate)
calculate_button.pack()
# Вкладка "Чекбоксы"
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

def show_selection():
    selection = ""
    if var1.get() == 1:
        selection += "Первый "
    if var2.get() == 1:
        selection += "Второй "
    if var3.get() == 1:
        selection += "Третий"

    messagebox.showinfo("Выбор", f"Вы выбрали: {selection}")

checkbox1 = tk.Checkbutton(tab2, text="Первый", variable=var1)
checkbox1.pack()

checkbox2 = tk.Checkbutton(tab2, text="Второй", variable=var2)
checkbox2.pack()

checkbox3 = tk.Checkbutton(tab2, text="Третий", variable=var3)
checkbox3.pack()

show_message_button = tk.Button(tab2, text="Показать выбор", command=show_selection)
show_message_button.pack()




# Вкладка "Работа с текстом"
text_entry = tk.Text(tab3)
text_entry.pack()

load_file_button = tk.Button(tab3, text="Загрузить файл", command=load_file)
load_file_button.pack()


# Запуск главного цикла
root.mainloop()
