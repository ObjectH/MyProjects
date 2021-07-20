from tkinter import *
from tkinter import messagebox
import math

# Переменные для корней уравнения
x1 = 0
x2 = 0
x3 = 0
x4 = 0

# Эти переменнные нужны для нахождения корней биквадратного уранения
t1 = 0
t2 = 0

#Окно программы
root = Tk()
root.geometry('500x500')
root.title('Calculator')
root.resizable(True, True)


# Интерфейс при выборе линейного уранения
def linear():
    # Элементы
    frame = Frame(root, bd=10)
    k_entry = Entry(frame)
    x_label = Label(frame, text='X')
    plus_label = Label(frame, text='+')
    b1_entry = Entry(frame)
    equals_label = Label(frame, text='=')
    y_entry = Entry(frame)
    button = Button(frame, text='OK', command=lambda: ok())
    answer_label = Label(frame, text='Ответ:')

    # Их положение
    frame.place(relx=0.5, rely=0.32, relwidth=0.8, relheight=0.6, anchor='n')
    k_entry.place(relx=0.15, rely=0.2, relwidth=0.1, relheight=0.1)
    x_label.place(relx=0.25, rely=0.2, relwidth=0.05, relheight=0.1)
    plus_label.place(relx=0.3, rely=0.2, relwidth=0.05, relheight=0.1)
    b1_entry.place(relx=0.35, rely=0.2, relwidth=0.1, relheight=0.1)
    equals_label.place(relx=0.45, rely=0.2, relwidth=0.05, relheight=0.1)
    y_entry.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.1)
    button.place(relx=0.65, rely=0.2, relheight=0.1, relwidth=0.1)
    answer_label.place(relx=0.15, rely=0.35)

    # Нахождение корня
    def ok():
        nonlocal k_entry
        nonlocal b1_entry
        nonlocal y_entry
        nonlocal answer_label
        global x1
        k = k_entry.get()
        b1 = b1_entry.get()
        y = y_entry.get()
        def trying():
            nonlocal k
            nonlocal b1
            nonlocal y
            try:
                float(k)
                float(b1)
                float(y)
                return True
            except ValueError:
                return False
        trying()
        if trying() == False:
            messagebox.showwarning('Warning', 'Вы уверены, что ввели числа?')
        else:
            k = float(k_entry.get())
            b1 = float(b1_entry.get())
            y = float(y_entry.get())
            if trying()==False:
                messagebox.showwarning('Warning', 'Вы уверены, что ввели числа?')
            if k != 0:
                pre_x = y - b1
                x1 = pre_x / k
                answer_label.config(text='Ответ: ' + ' x = ' + str(x1))
            else:
                if b1 == y:
                    answer_label.config(text='Ответ: любое число')
                else:
                    answer_label.config(text='Ответ: корней нет.')


# Интерфейс при выборе квадратного уравнения
def quadratic():
    # Элементы
    frame = Frame(root, bd=10)
    a2_entry = Entry(frame)
    x_2_label = Label(frame, text='X\u00B2')
    plus_label = Label(frame, text='+')
    b2_entry = Entry(frame)
    x_label = Label(frame, text='X')
    plus_label_2 = Label(frame, text='+')
    c2_entry = Entry(frame)
    equals_label = Label(frame, text='=')
    y2_entry = Entry(frame)
    button = Button(frame, text='OK', command=lambda: ok2())
    answer_label = Label(frame, text='Ответ:')

    # Их положение
    frame.place(relx=0.5, rely=0.32, relwidth=0.8, relheight=0.6, anchor='n')
    a2_entry.place(relx=0.1, rely=0.2, relwidth=0.1, relheight=0.1)
    x_2_label.place(relx=0.2, rely=0.2, relwidth=0.05, relheight=0.1)
    plus_label.place(relx=0.25, rely=0.2, relwidth=0.05, relheight=0.1)
    b2_entry.place(relx=0.3, rely=0.2, relwidth=0.1, relheight=0.1)
    x_label.place(relx=0.4, rely=0.2, relwidth=0.05, relheight=0.1)
    plus_label_2.place(relx=0.45, rely=0.2, relwidth=0.05, relheight=0.1)
    c2_entry.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.1)
    equals_label.place(relx=0.6, rely=0.2, relwidth=0.05, relheight=0.1)
    y2_entry.place(relx=0.65, rely=0.2, relwidth=0.1, relheight=0.1)
    button.place(relx=0.77, rely=0.2, relwidth=0.1, relheight=0.1)
    answer_label.place(relx=0.1, rely=0.35)

    # Нахождение корней квадратного уравнения(через дискриминант)
    def ok2():
        nonlocal a2_entry
        nonlocal b2_entry
        nonlocal c2_entry
        nonlocal y2_entry
        global x1
        global x2
        a2 = a2_entry.get()
        b2 = b2_entry.get()
        c2 = c2_entry.get()
        y2 = y2_entry.get()
        def trying():
            nonlocal a2
            nonlocal b2
            nonlocal c2
            nonlocal y2
            try:
                float(a2)
                float(b2)
                float(c2)
                float(y2)
                return True
            except ValueError:
                return False
        trying()
        if trying()==False:
            messagebox.showwarning('Warning', 'Вы уверены, что ввели числа?')
        else:
            a2 = float(a2_entry.get())
            b2 = float(b2_entry.get())
            c2 = float(c2_entry.get())
            y2 = float(y2_entry.get())
            if a2 == 0:
                messagebox.showwarning('Warning', 'Уравнение не квадратное!')
            else:
                if y2 != 0:
                    c2 = y2 - c2
                d = b2 ** 2 - 4 * a2 * c2
                if d < 0:
                    answer_label.config(text='Ответ: действительных корней нет.')
                else:
                    x1 = (b2 * -1 + math.sqrt(d)) / (a2 * 2)
                    x2 = (b2 * -1 - math.sqrt(d)) / (a2 * 2)
                    answer_label.config(text='Ответ: ' + str(x1) + '; ' +'\n'+'          '+ str(x2))


def biquadratic():
    # Элементы
    frame = Frame(root, bd=10)
    a4_entry = Entry(frame)
    x_4_label = Label(frame, text='X\u2074')
    plus_label = Label(frame, text='+')
    b4_entry = Entry(frame)
    x_2_label = Label(frame, text='X\u00B2')
    plus_label_2 = Label(frame, text='+')
    c4_entry = Entry(frame)
    equals_label = Label(frame, text='=')
    y4_entry = Entry(frame)
    button = Button(frame, text='OK', command=lambda: ok4())
    answer_label = Label(frame, text='Ответ:')

    # Их положение
    frame.place(relx=0.5, rely=0.32, relwidth=0.8, relheight=0.6, anchor='n')
    a4_entry.place(relx=0.1, rely=0.2, relwidth=0.1, relheight=0.1)
    x_4_label.place(relx=0.2, rely=0.2, relwidth=0.05, relheight=0.1)
    plus_label.place(relx=0.25, rely=0.2, relwidth=0.05, relheight=0.1)
    b4_entry.place(relx=0.3, rely=0.2, relwidth=0.1, relheight=0.1)
    x_2_label.place(relx=0.4, rely=0.2, relwidth=0.05, relheight=0.1)
    plus_label_2.place(relx=0.45, rely=0.2, relwidth=0.05, relheight=0.1)
    c4_entry.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.1)
    equals_label.place(relx=0.6, rely=0.2, relwidth=0.05, relheight=0.1)
    y4_entry.place(relx=0.65, rely=0.2, relwidth=0.1, relheight=0.1)
    button.place(relx=0.77, rely=0.2, relwidth=0.1, relheight=0.1)
    answer_label.place(relx=0.1, rely=0.35)

    def ok4():
        nonlocal a4_entry
        nonlocal b4_entry
        nonlocal c4_entry
        nonlocal y4_entry
        global x1
        global x2
        global x3
        global x4
        global t1
        global t2
        a4 = a4_entry.get()
        b4 = b4_entry.get()
        c4 = c4_entry.get()
        y4 = y4_entry.get()
        def trying():
            nonlocal a4
            nonlocal b4
            nonlocal c4
            nonlocal y4
            try:
                float(a4)
                float(b4)
                float(c4)
                float(y4)
                return True
            except ValueError:
                return False
        trying()
        if trying()==False:
            messagebox.showwarning('Warning', 'Вы уверены, что ввели числа?')
        else:
            a4 = float(a4)
            b4 = float(b4)
            c4 = float(c4)
            y4 = float(y4)
            if a4 == 0 or b4 == 0:
                messagebox.showwarning('Warning', 'Вам, скорее всего, нужен другой калькулятор.')
            else:
                if y4 != 0:
                    c4 = c4 - y4
                d = b4 ** 2 - 4 * a4 * c4
                if d < 0:
                    answer_label.config(text='Ответ: действительных корней нет.')
                else:
                    t1 = (b4 * -1 + math.sqrt(d)) / (a4 * 2)
                    t2 = (b4 * -1 - math.sqrt(d)) / (a4 * 2)
                    if t1 < 0 and t2 >= 0:
                        x1 = math.sqrt(t2)
                        x2 = x1 * -1
                        answer_label.config(text='Ответ: ' + str(x1) + '; ' + '\n'+'          '+ str(x2))
                    elif t2 < 0 and t1 >= 0:
                        x1 = math.sqrt(t1)
                        x2 = x1 * -1
                        answer_label.config(text='Ответ: ' + str(x1) + '; ' +'\n'+'          '+ str(x2))
                    elif 0 <= t2 and 0 <= t1 and t2 != t1:
                        x1 = math.sqrt(t1)
                        x2 = x1 * -1
                        x3 = math.sqrt(t2)
                        x4 = x3 * -1
                        answer_label.config(text='Ответ: ' + str(x2) + '; ' +'\n'+'          '+ str(x4) + '; ' +'\n'+'          '+ str(x1) + '; ' +'\n'+'          '+ str(x3))
                    elif 0 <= t2 and 0 <= t1 and t2 == t1:
                        x1 = math.sqrt(t1)
                        x2 = x1 * -1
                        answer_label.config(text='Ответ: ' + str(x1) + '; ' +'\n'+ '          '+str(x2))
                    else:
                        answer_label.config(text='Ответ: действительных корней нет')

# Фон фрейма, текста, полей ввода и шрифт
root.option_add('*Font', 'Calibri')
root.option_add('*Background', 'white')

# Фоновое изображение
img = PhotoImage(file='Фон.gif')
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

# Надпись
master_label = Label(root, text='Какое уравнение Вам нужно решить?', font=('Calibri', 16))
master_label.place(relx=0.095, rely=0.08, relheight=0.1, relwidth=0.81)

# Кнопки
button_lin = Button(root, text='Линейное', command=lambda: linear())
button_lin.place(relx=0.095, rely=0.2, relwidth=0.27, relheight=0.1)

button_quadratic = Button(root, text='Квадртное', command=lambda: quadratic())
button_quadratic.place(relx=0.365, rely=0.2, relwidth=0.27, relheight=0.1)

button_quartic = Button(root, text='Биквадратное', command=lambda: biquadratic())
button_quartic.place(relx=0.635, rely=0.2, relwidth=0.27, relheight=0.1)

root.mainloop()
