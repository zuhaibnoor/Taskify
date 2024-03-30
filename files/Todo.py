from customtkinter import *
from CTkMessagebox import CTkMessagebox

_row = 0

#function for adding tasks on the scrollframe
def add_task(scroll_frame, entry):
    task = entry.get().strip()
    if  task != '':
        print(task) ######################## debugging
        task_label = CTkLabel(scroll_frame, text = task)
        
        # placing the tasks/notes on the scrollframe by using the grid method. The global variable -
        # 'row' is used to update the rows for the complete instance of the application, not just on the - 
        # exection of this fucntion
        global _row
        task_label.grid(row = _row, column= 0)
        _row += 1
    entry.delete(0,END)

#ToDo: Add a function or implement logic for displaying the existing tasks/notes(if any) of the user upon logging in
