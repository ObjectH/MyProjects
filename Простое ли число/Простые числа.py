from tkinter import *
import math

# Окно программы
root = Tk()
root.title("Простое ли число?")
root.geometry("500x500")
root.resizable(False, False)
root.option_add('*Background', 'white')

# Фон
img=PhotoImage(file="photo.gif")
background_label=Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

# Надпись вверху
label = Label(root, text="Простое ли число?", font=('Calibri',24), fg='#5FC0CE')
label.place(relx=0.1,rely=0.1, relwidth=0.8, relheight=0.125)

# Рамка, внутри которой все элементы интерфейса 
frame = Frame(root, bd=10)
frame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.65)

# Надпись перед полем ввода
label_enter = Label(frame, text="Введите число:", font=('Calibri',16), fg='#5FC0CE')
label_enter.place(rely=0.2, relx=0.1, relwidth=0.35, relheight=0.1)

# Поле ввода
entry = Entry(frame, font=('Calibri',16), fg='#5FC0CE')
entry.place(relx=0.48, rely=0.2, relwidth=0.27, relheight=0.1)

# Поле вывода
answer_label = Text(frame, font=('Calibri',18), fg='#5FC0CE')
answer_label.place(relx=0.1, rely=0.33, relwidth=0.8, relheight = 0.6)

# Прокрутка поля вывода
scrollBar = Scrollbar(frame)
scrollBar.place(relx=0.9, rely=0.33, relheight=0.6)
scrollBar['command'] = answer_label.yview
answer_label['yscrollcommand'] = scrollBar.set

# Функция для определения множителей и того, является ли число простым
def check():
    isSimple = "" # Часть текста ответа, отвечающая за тип числа
    answer = "" # Текст ответа
    simple = True # Переменная для определеления типа числа
    isInteger = True # Переменная для проверки корректности ввода
    answer_label.delete('1.0', END) # Очистка поля вывода
    num = entry.get() # Получение введённого числа
    mul = "Множители:" # Часть текста ответа, отвечающая за множители
    
    # Я разделила текст ответа на две части, чтобы было удобнее сделать перенос строк

    # Проверка на корректность ввода
    try:
        int(num)
        isInteger = True
    except ValueError:
        isInteger = False
    # Сообщение о некорректности ввода
    if not isInteger:
        answer="Похоже, Вы ввели не \nчисло или же дробное\nчисло, а дробные числа\nнельзя отнести к простым\nили составным."
    # Если ввод был корректным, то выполнится следующий код
    else:
        # Преобразование к типу int 
        num_int = int(num)
        # Ответ при вводе единицы
        if num_int == 1:
            isSimple="Вы ввели число 1,\nоно не является ни\nпростым, ни составным"
        #  Ответ при вводе неположительного числа
        elif num_int < 1:
            answer="Это точно не простое\nчисло, потому что оно\nне положительное"
        # Код, который выполняется для натуральных чисел
        else:
            # Для каждого из натуральных чисел, меньших чем данное (кроме 1),
            # выполныется проверка, делится ли на него данное число,
            # и если да, то число составное
            for i in range(2, num_int):
                ostatok = num_int%i
                if ostatok != 0:
                    simple = True
                else:
                    simple = False
                    isSimple = "Число составное"
                    break
            if simple:
                isSimple = "Число простое"
        # Определение множителей
        if num_int > 0:
            # Проверка, "помещается" ли число в тип integer
            if num_int <= 2147483647:
                # Если число делится на одно из чисел, меньших, чем оно,
                # то прибавляется новый множитель
                for i in range(1, num_int+1):
                    if num_int%i==0:
                        mul += " "+str(i)+","
                    else:
                        continue
                    # В конец добавляется точка
                    if i == num_int:
                        mul = mul[0:-1]+"."
                        # После каждого 15-го символа перенос строки
                        for j in range(0, len(mul)):
                            if j%15 == 0:
                                if mul[j-1] == ' ':
                                    mul = mul[:j]+'\n'+mul[j:]
                        answer = isSimple+"\n"+mul
            # Ответ, если число не "помещается" в тип integer
            else:
                answer = "Слишком большое число"
    # Вывод ответа
    answer_label.insert(END, answer)

# Кнопка
button = Button(frame, font=('Calibri',16), fg='#5FC0CE', text="OK", command=lambda:check())
button.place(relx=0.78, rely=0.2, relheight=0.1, relwidth=0.12)

# Главный цикл программы
root.mainloop()
