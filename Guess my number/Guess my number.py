"""
Это игра "Угадай число". Компьютер загадывает число, а пользователь отгадывает. В игре 3 партии, в каждой из них
пользователю даётся три попытки. Если пользователь за одну партию смог угадать число, он получает 1 очко,
если нет - очко получает компьютер.
Есть 3 поля ввода. Первое - для ввода минимального числа, которое может загадать компьютер, второе - для максимального числа
и третье - для ввода ответа. Над ними выводятся номер попытки, номер партии и счёт, под ними - информация о том, угадал
пользователь или нет. Планировалось сделать так, чтобы вместе с ответом компьютера на ответ пользователя менялась картинка,
но не сложилось, может, потом доделаю.
"""

import random
import tkinter
from tkinter import messagebox

user_score = 0  # Баллы пользователя
comp_score = 0  # Баллы компьютера
attempt = 0  # Номер попытки
game = 1  # Номер партии
comp_num = 0  # Число, которое загадал компьютер
user_num = 0  # Ответ пользователя
isCorrect = True  # Для проверки на корректность ввода
isGuessed = False  # Для поверки, угадал пользователь или нет

# Окно программы
root = tkinter.Tk()
root.geometry('500x500')
root.resizable(False, False)
root.title('Угадай число')

# Надпись с названием игры
label_title = tkinter.Label(root, text='Угадай число', bg='#BFD7EA', fg='#508CA4', font=('Calibri', 30))
label_title.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)

# Рамка, внутри которой все элементы пользовательского интерфейса
frame = tkinter.Frame(root, bg='#FFFFFF')
frame.place(relx=0.05, rely=0.17, relwidth=0.9, relheight=0.78)

# Номер попытки
label_attempt_number = tkinter.Label(frame, text='Попытка: 0', bg='#BFD7EA', fg='#508CA4', font=('Calibri', 14))
label_attempt_number.place(relx=0.03, rely=0.03, relwidth=0.2, relheight=0.05)

# Номер партии
label_game_number = tkinter.Label(frame, text='Партия: 0', bg='#BFD7EA', fg='#508CA4', font=('Calibri', 14))
label_game_number.place(relx=0.24, rely=0.03, relwidth=0.2, relheight=0.05)

# Счёт
label_score = tkinter.Label(frame, text='Счёт: 0-0', bg='#BFD7EA', fg='#508CA4', font=('Calibri', 14))
label_score.place(relx=0.45, rely=0.03, relwidth=0.2, relheight=0.05)

# Подсказка поля ввода для нижней границы
label_min_num = tkinter.Label(frame, text='Введите минимальное число:', bg='#FFFFFF', fg='#508CA4',
                              font=('Calibri', 15))
label_min_num.place(relx=0.03, rely=0.1, relwidth=0.62, relheight=0.07)

# Подсказка поля ввода для верхней границы
label_max_num = tkinter.Label(frame, text='Введите максимальное число:', bg='#FFFFFF', fg='#508CA4',
                              font=('Calibri', 15))
label_max_num.place(relx=0.03, rely=0.18, relwidth=0.62, relheight=0.07)

# Подсказка поля ввода для ответа
label_min_num = tkinter.Label(frame, text='Какое число было задумано?', bg='#FFFFFF', fg='#508CA4',
                              font=('Calibri', 15))
label_min_num.place(relx=0.03, rely=0.26, relwidth=0.62, relheight=0.07)

# Поле ввода для нижней границы
entry_min_num = tkinter.Entry(frame, bg='#FFFFFF', fg='#508CA4', font=('Calibri', 18))
entry_min_num.place(relx=0.65, rely=0.1, relwidth=0.2, relheight=0.07)

# Поле ввода для верхней границы
entry_max_num = tkinter.Entry(frame, bg='#FFFFFF', fg='#508CA4', font=('Calibri', 18))
entry_max_num.place(relx=0.65, rely=0.18, relwidth=0.2, relheight=0.07)

# Поле ввода для ответа пользователя
entry_user_num = tkinter.Entry(frame, bg='#FFFFFF', fg='#508CA4', font=('Calibri', 18))
entry_user_num.place(relx=0.65, rely=0.26, relwidth=0.2, relheight=0.07)

# Место для ответа компьютера на ввод пользователя
answer_label = tkinter.Label(frame, bg='#FFFFFF', fg='#508CA4', font=('Calibri', 18), text='')
answer_label.place(relx=0.03, rely=0.34, relwidth=0.94, relheight=0.07)

# Место для вывода победителя
winner_label = tkinter.Label(frame, bg='#FFFFFF', fg='#508CA4', font=('Calibri', 18), text='')
winner_label.place(relx=0.03, rely=0.42, relwidth=0.94, relheight=0.07)

# Картинка
img = tkinter.PhotoImage(file="img_normal.gif")
image_label = tkinter.Label(frame, image=img, bg="#FFFFFF")
image_label.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.37)


# Функция для новой попытки
def comp_number():
    global isCorrect
    global comp_num
    global game
    global attempt
    # Получение нижней и верхней границы
    num_min_str = entry_min_num.get()
    num_max_str = entry_max_num.get()
    # Проверка на корректность ввода
    try:
        int(num_min_str)
        int(num_max_str)
    except ValueError:
        isCorrect = False
        messagebox.showwarning('Warning', 'Некорректный ввод')
    if isCorrect:
        # Вывод счёта, номера партии и попытки, изменение номера попытки
        label_score.config(text="Счёт: " + " " + str(user_score) + "-" + str(comp_score))
        attempt += 1
        label_attempt_number.config(text="Попытка: " + str(attempt))
        label_game_number.config(text="Партия: " + str(game))
        num_min = int(num_min_str)
        num_max = int(num_max_str)
        if num_min >= num_max:
            messagebox.showwarning('Warning', "Верхняя граница должна быть больше нижней!")
            isCorrect = False
        # Выбор числа компьютером
        else:
            comp_num = random.randint(num_min, num_max)
    return True


# Функция для работы с ответом пользователя - проверкой на корректность, совпадение с загаданным числом,
# в случае необходимости - переход к новой партии
def play():
    global isCorrect
    global user_num
    global attempt
    global comp_score
    global user_score
    global game
    global comp_score
    global isGuessed
    # Получение ответа
    user_num_str = entry_user_num.get()
    # Проверка на корректность ввода
    try:
        user_num = int(user_num_str)
    except ValueError:
        isCorrect = False
        messagebox.showwarning('Warning', 'Некорректный ввод')
    if isCorrect:
        # Проверка, угадал ли пользователь, вывод её результата
        # Пользователь не угадал
        if user_num > comp_num:
            answer_label.config(text="Загаданное число меньше")
            entry_user_num.delete(0, tkinter.END)
            attempt += 1
            isGuessed = False
        elif user_num < comp_num:
            answer_label.config(text="Загаданное число больше")
            entry_user_num.delete(0, tkinter.END)
            isGuessed = False
            attempt += 1
        # Пользователь угадал, но партия не последняя
        elif user_num == comp_num and game < 3:
            game += 1
            answer_label.config(text="Вы угадали!")
            attempt = 0
            user_score += 1
            entry_user_num.delete(0, tkinter.END)
            entry_min_num.delete(0, tkinter.END)
            entry_max_num.delete(0, tkinter.END)
        # Пользоваетель угадал и партия последняя
        else:
            answer_label.config(text="Вы угадали!")
            attempt = 0
            user_score += 1
            isGuessed = True
        # Пользователь не угадал ни разу за партию, партия не последняя
        if attempt == 4 and game < 3 and not isGuessed:
            game += 1
            answer_label.config(text="Было загадано число" + " " + str(comp_num))
            attempt = 0
            comp_score += 1
            entry_user_num.delete(0, tkinter.END)
            entry_min_num.delete(0, tkinter.END)
            entry_max_num.delete(0, tkinter.END)
        # То же самое, но партия последняя
        if attempt == 4 and game == 3 and not isGuessed:
            answer_label.config(text="Было загадано число" + " " + str(comp_num))
            attempt = 0
            comp_score += 1
        # Вывод результатов
        label_score.config(text="Счёт: " + " " + str(user_score) + "-" + str(comp_score))
        label_attempt_number.config(text="Попытка: " + str(attempt))
        label_game_number.config(text="Партия: " + str(game))
        if game == 3:
            if attempt == 3 or isGuessed:
                if comp_score > user_score:
                    winner_label.config(text="Компьютер победил")
                elif comp_score < user_score:
                    winner_label.config(text="Поздравляем, Вы победили!")
                else:
                    winner_label.config(text="Ничья!")


# Если пользователь передумал продолжать игру, он может начать новую
def new_game():
    # Просто выставляем всем переменным и надписям изначальное значение
    global isCorrect
    global user_num
    global attempt
    global comp_score
    global user_score
    global game
    global comp_score
    global isGuessed
    isCorrect = True
    isGuessed = False
    user_score = 0
    comp_score = 0
    game = 1
    attempt = 0
    entry_user_num.delete(0, tkinter.END)
    entry_min_num.delete(0, tkinter.END)
    entry_max_num.delete(0, tkinter.END)
    label_game_number.config(text="Партия: 0")
    label_attempt_number.config(text="Попытка: " + str(attempt))
    label_score.config(text="Счёт: 0-0")
    answer_label.config(text="")
    winner_label.config(text="")


# Кнопка для начала новой игры
button_new_game = tkinter.Button(frame, bg='#A2BFD2', fg='#508CA4', command=lambda: new_game(), font=('Calibri', 18),
                                 text='Новая игра')
button_new_game.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.07)

# Кнопка для загадывания числа
button_comp_num = tkinter.Button(frame, bg='#A2BFD2', fg='#508CA4', command=lambda: comp_number(), font=('Calibri', 18),
                                 text='OK')
button_comp_num.place(relx=0.86, rely=0.1, relwidth=0.11, relheight=0.15)

# Кнопка для отправки ответа
button_user_num = tkinter.Button(frame, bg='#A2BFD2', fg='#508CA4', command=lambda: play(), font=('Calibri', 18),
                                 text='OK')
button_user_num.place(relx=0.86, rely=0.26, relwidth=0.11, relheight=0.07)

root.mainloop()
