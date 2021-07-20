import random
from tkinter import *
from tkinter import messagebox

user_score = 0
comp_score = 0
attempt = 0
game = 1
comp_num = 0
user_num = 0
isCorrect = True
isGuessed = False


root = Tk()
root.geometry('500x500')
root.resizable(False, False)
root.title('Угадай число')

label_title = Label(root, text = 'Угадай число', bg = '#BFD7EA', fg = '#508CA4', font = ('Colibri', 30))
label_title.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.1)

frame = Frame(root, bg = '#FFFFFF')
frame.place(relx = 0.05, rely = 0.17, relwidth = 0.9, relheight = 0.78)

label_attempt_number = Label(frame, text = 'Попытка: 0', bg = '#BFD7EA', fg = '#508CA4', font = ('Calibri', 14))
label_attempt_number.place(relx = 0.03, rely = 0.03, relwidth = 0.2, relheight = 0.05)

label_game_number = Label(frame, text = 'Партия: 0', bg = '#BFD7EA', fg = '#508CA4', font = ('Calibri', 14))
label_game_number.place(relx = 0.24, rely = 0.03, relwidth = 0.2, relheight = 0.05)

label_score = Label(frame, text = 'Счёт: 0-0', bg = '#BFD7EA', fg = '#508CA4', font = ('Calibri', 14))
label_score.place(relx = 0.45, rely = 0.03, relwidth = 0.2, relheight = 0.05)

label_min_num = Label(frame, text = 'Введите минимальное число:', bg = '#FFFFFF', fg ='#508CA4', font = ('Colibri', 15))
label_min_num.place(relx = 0.03, rely = 0.1, relwidth = 0.62, relheight = 0.07)

label_max_num = Label(frame, text = 'Введите максимальное число:', bg = '#FFFFFF', fg ='#508CA4', font = ('Colibri', 15))
label_max_num.place(relx = 0.03, rely = 0.18, relwidth = 0.62, relheight = 0.07)

label_min_num = Label(frame, text = 'Какое число было задумано?', bg = '#FFFFFF', fg ='#508CA4', font = ('Colibri', 15))
label_min_num.place(relx = 0.03, rely = 0.26, relwidth = 0.62, relheight = 0.07)

entry_min_num = Entry(frame, bg = '#FFFFFF', fg = '#508CA4', font = ('Calibri', 18))
entry_min_num.place(relx = 0.65, rely = 0.1, relwidth = 0.2, relheight = 0.07)

entry_max_num = Entry(frame, bg = '#FFFFFF', fg = '#508CA4', font = ('Calibri', 18))
entry_max_num.place(relx = 0.65, rely = 0.18, relwidth = 0.2, relheight = 0.07)

entry_user_num = Entry(frame, bg = '#FFFFFF', fg = '#508CA4', font = ('Calibri', 18))
entry_user_num.place(relx = 0.65, rely = 0.26, relwidth = 0.2, relheight = 0.07)

answer_label = Label(frame, bg = '#FFFFFF', fg = '#508CA4', font = ('Calibri', 18), text = '') 
answer_label.place(relx = 0.03, rely = 0.34, relwidth = 0.94, relheight = 0.07)

winner_label = Label(frame, bg = '#FFFFFF', fg = '#508CA4', font = ('Calibri', 18), text = '') 
winner_label.place(relx = 0.03, rely = 0.42, relwidth = 0.94, relheight = 0.07)

img = PhotoImage(file = "img_normal.gif")
image_label = Label(frame, image = img, bg="#FFFFFF")
image_label.place(relx = 0.05, rely = 0.5, relwidth = 0.9, relheight = 0.37)

def comp_number():
    global isCorrect
    global comp_num
    global game
    global attempt
    num_min_str = entry_min_num.get()
    num_max_str = entry_max_num.get()
    try:
        int(num_min_str)
        int(num_max_str)
    except ValueError:
        isCorrect = False
        messagebox.showwarning('Warning', 'Некорректный ввод')
    if isCorrect == True:
        label_score.config(text="Счёт: "+" "+str(user_score)+"-"+str(comp_score))
        attempt += 1
        label_attempt_number.config(text="Попытка: "+str(attempt))
        label_game_number.config(text="Партия: "+str(game))        
        num_min = int(num_min_str)
        num_max = int(num_max_str)
        if num_min >= num_max:
            messagebox.showwarning('Warning', "Верхняя граница должна быть больше нижней!")
            isCorrect = False
        else:
            comp_num = random.randint(num_min, num_max)
    return True


def play():
    global isCorrect
    global user_num
    global attempt
    global comp_score
    global user_score
    global game
    global comp_score
    global isGuessed
    user_num_str = entry_user_num.get()
    try:
        int(user_num_str)
    except ValueError:
        isCorrect = False
        messagebox.showwarning('Warning', 'Некорректный ввод')
    if isCorrect == True:
        user_num = int(user_num_str)
        if user_num > comp_num:
            answer_label.config(text="Загаданное число меньше")
            entry_user_num.delete(0, END)
            attempt += 1           
            isGuessed = False
        elif user_num < comp_num:
            answer_label.config(text="Загаданное число больше")
            entry_user_num.delete(0, END)
            isGuessed = False
            attempt += 1
        elif user_num == comp_num and game < 3:
            game += 1
            answer_label.config(text="Вы угадали!")
            attempt = 0
            user_score += 1
            entry_user_num.delete(0, END)
            entry_min_num.delete(0, END)
            entry_max_num.delete(0, END)
        else:
            answer_label.config(text="Вы угадали!")
            attempt = 0
            user_score += 1
            isGuessed = True
        if attempt == 4 and isGuessed == False and game < 3:
            game += 1
            answer_label.config(text="Было загадано число"+" "+str(comp_num))
            attempt = 0
            comp_score += 1
            entry_user_num.delete(0, END)
            entry_min_num.delete(0, END)
            entry_max_num.delete(0, END)
        if attempt == 4 and isGuessed == False and game == 3:
            answer_label.config(text="Было загадано число"+" "+str(comp_num))
            attempt = 0
            comp_score += 1            
        label_score.config(text="Счёт: "+" "+str(user_score)+"-"+str(comp_score))
        label_attempt_number.config(text="Попытка: "+str(attempt))
        label_game_number.config(text="Партия: "+str(game))
        if game == 3 and attempt == 3:
            if comp_score > user_score:
                winner_label.config(text="Компьютер победил")
            elif comp_score < user_score:
                winner_label.config(text="Поздравляем, Вы победили!")
            else:
                winner_label.config(text="Ничья!")
        if game == 3 and isGuessed == True:
            if comp_score > user_score:
                winner_label.config(text="Компьютер победил")
            elif comp_score < user_score:
                winner_label.config(text="Поздравляем, Вы победили!")
            else:
                winner_label.config(text="Ничья!")


def new_game():
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
    entry_user_num.delete(0, END)
    entry_min_num.delete(0, END)
    entry_max_num.delete(0, END)
    label_game_number.config(text="Партия: 0")
    label_attempt_number.config(text="Попытка: "+str(attempt))
    label_score.config(text="Счёт: 0-0")
    answer_label.config(text="")
    winner_label.config(text="")



button_new_game = Button(frame, bg = '#A2BFD2', fg = '#508CA4', command = lambda: new_game(), font = ('Calibri', 18), text = 'Новая игра')
button_new_game.place(relx = 0.35, rely = 0.9, relwidth = 0.3, relheight = 0.07)     

button_comp_num = Button(frame, bg = '#A2BFD2', fg = '#508CA4', command = lambda: comp_number(), font = ('Calibri', 18), text = 'OK')
button_comp_num.place(relx = 0.86, rely = 0.1, relwidth = 0.11, relheight = 0.15)

button_user_num = Button(frame, bg = '#A2BFD2', fg = '#508CA4', command = lambda: play(), font = ('Calibri', 18), text = 'OK')
button_user_num.place(relx = 0.86, rely = 0.26, relwidth = 0.11, relheight = 0.07)

root.mainloop()
