from customtkinter import *
from CTkMessagebox import CTkMessagebox


#function for adding new tasks on the scrollframe
def add_task(scroll_frame, entry, UserName):
    task = entry.get().strip()
    if  task != '':
        with open(f'files/users/{UserName}.txt') as f:
            user_info = f.read()
            user_info = eval(user_info)
            task_label = CTkLabel(scroll_frame, text= f'{user_info["rows"]} : {task}')
            task_label.grid(row = user_info['rows']-1, column = 0 )
            print(user_info['rows'])
            
            user_info[user_info['rows']-1] = task
            user_info['rows'] += 1
            
            with open(f'files/users/{UserName}.txt', 'w') as f:
                f.write(str(user_info))
    entry.delete(0,END)


#function for adding existing tasks on the scrollframe
def add_existing_tasks(scrl_frm, UserName):
    with open(f'files/users/{UserName}.txt') as f:
        user_info = f.read()
        user_info = eval(user_info)
        user_info.pop(UserName)
        user_info.pop('rows')
        rows = 1
        for i in user_info:
            task_label = CTkLabel(scrl_frm, text= f'{rows} : {user_info[i]}')
            task_label.grid(row = i, column = 0)
            rows += 1 


