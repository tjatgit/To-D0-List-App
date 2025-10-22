'''
Simple To-Do List app
Topics: tkinter, grid geometry manager
Listbox widget, scrollbar widget, tkinter.messagebox,pickle module, Try/Except Blocks.
'''


import tkinter
from tkinter import messagebox
import pickle #imported pickle module for dumping the data into a  file and loading.

root = tkinter.Tk()
root.title("To-Do List")

# Below are the functions for all the four task buttons.
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END,task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="You must enter a task.")
        
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="You must select a task.")

def load_task():
    try:
        tasks = pickle.load(open("tasks.txt","rb")) #loading the tasks from file using pickle and in rad in binary format.
        listbox_tasks.delete(0,tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END,task)
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="cannot find tasks.txt")


def save_task():
    tasks = listbox_tasks.get(0,listbox_tasks.size())
    pickle.dump(tasks,open("tasks.txt","wb")) #used pickle module for dumping the data into a file and in write in binary format.
    
    
#create a frame to store entry_tasks and scroolbar
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

#adding the scrollbar for listbox_tasks
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT,fill=tkinter.Y)

#Here entered tasks will be listed.
listbox_tasks = tkinter.Listbox(frame_tasks,height=10,width=50)
listbox_tasks.pack(side=tkinter.LEFT)

#setting the scrollbar for listed items for vieeing in y direction.
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

#Screen for entering the tasks.
entry_task = tkinter.Entry(root,width=48)
entry_task.pack()

#Buttons for adding,deleting,loading and saving tasks.
button_add_task = tkinter.Button(root,text="Add Task",width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root,text="Delete Task",width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root,text="load Tasks",width=48, command=load_task)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root,text="save Task",width=48, command=save_task)
button_save_tasks.pack()

root.mainloop()