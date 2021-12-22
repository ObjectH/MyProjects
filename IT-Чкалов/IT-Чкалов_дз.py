filtred = [] #список для "сглаженных" значений

#Считывание данных
f = open("in.txt")
string_input = f.read()
f.close()

"""Т. к. каждой точке присваивается среднее арифметическое нескольких
соседних значений, следующая пременнная отвечает за количество значений,
для которых находится среднее арифметическое"""
filtration = 10;

#Преобразование данных, полученных в виде строки, в список
data = string_input.split("\n")

#Число значений записываем в отдельную переменную и убираем из списка
number = int(data[0])

data = data[1::]

#Преобразование данных в вещественные числа
for i in range(0, number):
    data[i] = float(data[i])

"""Находим среднее арифметическое 10 соседних значений и записываем в текущий
элемент списка"""

"""Если элемент близко к концу, то среднее арифметическое находится для всех
    тех значений, которые стоят после него"""
for i in range(0, number):
    summa = 0
    if i < len(data) - filtration:
        for j in range(0, filtration):
            summa += data[i+j]
        filtred.append(summa / filtration)
    else:
        for j in range(0, len(data)-i):
            summa += data[i+j]
        filtred.append(summa / (len(data)-i))

#Преобразование данных в строку для записи в файл
text = ""    
for i in range(0, number):
    text += str(filtred[i]) + "\n"

#Запись ответа в файл
f = open("out.txt", "w")
f.write(text)
f.close()
