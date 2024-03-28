from customtkinter import *
from CTkMessagebox import CTkMessagebox

def add_task(scroll_frame, entry):
    task = entry.get()
    if  task != '':
        entry.delete(0,END)
        print(task)
        task_label = CTkLabel(scroll_frame, text= task)
        
        