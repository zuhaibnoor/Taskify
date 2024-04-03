from customtkinter import *
from CTkMessagebox import CTkMessagebox

## STATUS: Read/write operations: successful, add_task() fn working fine, add_existing_tasks() having trouble updating the "_row" var
## Todo:FIX THE "_row" var. The global variable "_row"  is not changing value in add_existing_task() function


_row = 0       ####### Debugging

#function for adding tasks on the scrollframe
def add_task(scroll_frame, entry, UserName):
    task = entry.get().strip()
    if  task != '':
        # print(task) ######################## debugging
        task_label = CTkLabel(scroll_frame, text = task)
        
        # placing the tasks/notes on the scrollframe by using the grid method. The global variable -
        # 'row' is used to update the rows for the complete instance of the application, not just on the - 
        # exection of this function
        
        global _row  
        task_label.grid(row = _row, column = 0)
        _row += 1
        with open(f'files/users/{UserName}.txt') as user_file:
            user_info = user_file.read()
            user_info  = eval(user_info)
            print('\n\n',user_info)   ######################## debugging
        user_info[_row] = task
        # print(user_info)    ######################## debugging
        with open(f'files/users/{UserName}.txt', 'w') as file:     ######################## debugging</>
            file.write(str(user_info))        ######################## debugging</>
        print(user_info)    ######################## debugging
    entry.delete(0,END)


#ToDo: Add a function or implement logic for displaying the existing tasks/notes(if any) of the user upon logging in

#-----------------------------Not final------------------------------
def add_existing_tasks(scrl_frm, UserName):
    with open(f"files/users/{UserName}.txt") as user_file:
        user_info  = user_file.read()
        user_info = eval(user_info)
        user_info.pop(UserName)                             ##### PROBLEMS
        global _row
        for i in user_info:
            task_label = CTkLabel(scrl_frm, text = f'{i} : {user_info[i]}')
            task_label.grid(row = _row, column = 0)
            _row += 1

#-----------------------------Not final------------------------------            

