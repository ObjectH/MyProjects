from tkinter import *
from tkinter import messagebox
import random
import pickle
import os

tasks=[]

root = Tk()
root.title('My Super To-Do  List')
root.geometry('600x550')
root.resizable(False, False)

img = PhotoImage(file='The background for the sign up form.gif')
background_label = Label(root, image=img)
background_label.place(relheight=1, relwidth=1)

frame = Frame(root, bd=10)
frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

listbox=Listbox(frame)
listbox.place(relx=0.32, rely=0.2, relwidth=0.67, relheight=0.78)

entry = Entry(frame, width=15)
entry.place(relx=0.32, rely=0.1, relwidth=0.67, relheight=0.07)

label_display = Label(frame, text='')
label_display.place(relx=0.3, rely=0.1)

label_title = Label(frame, text='My super To-do list', fg='dark blue', font='{Comic Sans MS} 16')
label_title.place(relx=0.3)

root.option_add('*Font', '{Comic Sans MS} 10')
root.option_add('*Background', 'white')

def save():
    data = tasks
    f = open('TODO.txt', 'w+')
    f.seek(0)
    f.close()
    f = open('TODO.txt', 'wb')
    pickle.dump(data, f)
    f.close()

def start(event):
    f = open('TODO.txt', 'rb+')
    c = os.stat('TODO.txt').st_size
    if c > 0:
        a = str(pickle.load(f))
        a = a.replace("'", "")
        a = a.replace("[", "")
        a = a.replace("]", "")
        b = a.split(',')
        tasks = b
        for i in tasks:
            listbox.insert(0, i)
    else:
        messagebox.showwarning('Warning', 'You have not any tasks')
    f.close()
    
def update_listbox():
    listbox.delete(0, END)
    for i in tasks:
        listbox.insert(0, i)

def add_task():
    task = entry.get()
    if task != '':
        tasks.append(task)
        update_listbox()
        entry.delete(0, END)
    else:
        messagebox.showwarning('Warning', 'Enter a task in the input box, please')
        entry.delete(0, END)
    
def del_one():
    task = listbox.get('active')
    if task in tasks:
        tasks.remove(task)
    update_listbox()
    
def del_all():
    confirmed = messagebox.askyesno('Please, confirm', 'Do you really want to delete all tasks?')
    if confirmed:
        global tasks
        tasks = []
        update_listbox()

def sort_asc():
    tasks.sort()
    update_listbox()
    
def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()

def choose_random():
    if len(tasks) > 0:
        task = random.choice(tasks)
        label_display['text'] = task
    else:
        messagebox.showwarning('Warning', 'There are no tasks in the list')

def show_number_of_tasks():
    number_of_tasks = len(tasks)
    message = 'Number of tasks: %s' % number_of_tasks
    label_display['text'] = message

button_desc = Button(frame, text='Sort A-Z', command=sort_desc)
button_desc.place(rely=0.4, relwidth=0.28)

button_sort_asc = Button(frame, text='Sort Z-A', command=sort_asc)
button_sort_asc.place(rely=0.5, relwidth=0.28)
        
button_add_task = Button(frame,text='Add task', command=add_task)
button_add_task.place(rely=0.1, relwidth=0.28)

button_del = Button(frame, text='Delete', command=del_one)
button_del.place(rely=0.2, relwidth=0.28)

button_del_all = Button(frame, text='Delete all tasks', command=del_all)
button_del_all.place(rely=0.3, relwidth=0.28)

button_choose_random = Button(frame, text='Random task', command=choose_random)
button_choose_random.place(rely=0.6, relwidth=0.28)

button_show_number_of_task = Button(frame, text='Count the tasks', command=show_number_of_tasks)
button_show_number_of_task.place(rely=0.7, relwidth=0.28)

button_save = Button(frame, text='Save', command = save)
button_save.place(rely=0.8, relwidth=0.28)

button_exit = Button(frame, text='Exit', command = exit)
button_exit.place(rely=0.9, relwidth=0.28)

root.bind('<Return>', start)

root.mainloop()
