from customtkinter import *
from CTkMessagebox import CTkMessagebox

_row = 0
def add_task(scroll_frame, entry):
    task = entry.get().strip()
    if  task != '':
        print(task)
        task_label = CTkLabel(scroll_frame, text = task)
        # _column = 0
        global _row
        task_label.grid(row = _row, column= 0)
        _row += 1
    entry.delete(0,END)

