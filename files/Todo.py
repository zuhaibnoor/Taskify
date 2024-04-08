from customtkinter import *
from CTkMessagebox import CTkMessagebox
import textwrap

# function for displaying an item of the to do list on the scrollframe
def create_label(frame, task, row):

    # wrapping the text incase it is too long to display on a single line in a label
    if len(task) >= 30:
        task = textwrap.wrap(task, width = 30) 
        for i in range(len(task)):
            task[i] = task[i]+'\n'

        task = " ".join(task)

    # the row no. and task are placed in this frame
    parent_frame = CTkFrame(frame,
                            fg_color="#2C2435",
                            border_color = "white")
    parent_frame.grid(row = row, column = 0, padx = 10, pady = 10)
    
    # the row no. label
    row_label = CTkLabel(parent_frame,
                         text = str(row+1),
                         font = CTkFont(size = 17, weight="bold"),
                         corner_radius = 20,
                         fg_color = "#008836")
    row_label.grid(row = 0,
                   column = 0,
                   padx = 7,
                   pady = 7,
                   ipadx = 5,
                   ipady = 5)

    # the item/task label
    task_label = CTkLabel(parent_frame, 
                          text = task,
                          font = CTkFont(size = 17),
                          corner_radius = 20,
                          fg_color = "#2C2435",
                          width=350, anchor="w")
    task_label.grid(row = 0,
                    column = 1,
                    padx = 7,
                    pady = 7,
                    ipadx = 5,
                    ipady = 5)



#function for adding new tasks on the scrollframe
def add_task(scroll_frame, entry, UserName):
    
    # taking the task as string and removing any extra spaces from beginning and end
    task = entry.get().strip()
    
    # if the task is a null string then it wont be saved in the file and wont be displayed on the scrollframe
    if  task != '':

        with open(f'files/users/{UserName}.txt') as f:
            user_info = f.read()
            user_info = eval(user_info)

            
            
             # The "rows" stored in the file start from 1, therefore for customtkinter, we have done- 
             # user_info["rows"]-1 because we have to provide rows that start from 0 for it to be placed
            
            create_label(scroll_frame,task, user_info['rows']-1)
           

            #------saving the task in the user_info dictionary----------
            user_info[user_info['rows']-1] = task
            user_info['rows'] += 1

            #----writing the new task added by the user in the file----
            with open(f'files/users/{UserName}.txt', 'w') as f:
                f.write(str(user_info))

    entry.delete(0,END)


#function for adding existing tasks on the scrollframe
def add_existing_tasks(scrl_frm, UserName):
    with open(f'files/users/{UserName}.txt') as f:
        user_info = f.read()
        user_info = eval(user_info)
        
        #removing the unnecessary info from the user_info
        user_info.pop(UserName)
        user_info.pop('rows')

        if user_info != {}:
            rows = 1

            # placing each item on the scroll frame
            for i in user_info:
                create_label(scrl_frm, user_info[i], i)
                rows += 1 


# function for deleting an item from the list
def delete_task(scroll_frame, user_name):

    # input dialog box for taking the item no. as input
    popup = CTkInputDialog(text = "Delete item No.",
                           button_fg_color="#9E0000",
                           button_hover_color="#7A0303")    
    task_no = popup.get_input()

    if task_no is not None:

        task_no = (int(task_no)) - 1

        # opening the user file
        with open(f'files/users/{user_name}.txt') as f:
            f = f.read()
            user_info = eval(f)

            # popping out the necessary info from the user file
            user_pwd = user_info.pop(user_name)
            rows = (user_info.pop("rows")) - 1

            # checking the presence of the entered task number in user_info
            if task_no in user_info:

                # deleting the entered task/item no.
                user_info.pop(task_no)
                
                # --------The order of numbering the task will be disturbed once an item is deleted-----
                #----------- Hence, reordering the items -----------------------------
            
                # appending all the items in a temporary list by a loop,
                # and then assigning them new row numbers
                temp_task_ls = []            
                for i in user_info:
                    temp_task_ls.append(user_info[i])
                new_user_info = {}
                new_user_info[user_name] = user_pwd
                new_user_info['rows'] = rows
                row = 0
                for task in temp_task_ls:
                    new_user_info[row] = task
                    row += 1

                # writing the updated items in the file once the deleting has been done
                with open(f'files/users/{user_name}.txt', 'w') as file:
                    file.write(str(new_user_info))

                # deleting the older item from the scrollframe display and then redisplaying
                # the updated items on the scroll frame using the "add_existing_tasks()"
                # function
                scroll_frame_children = scroll_frame.winfo_children()   #winfo_children() function returns a list of children widgets in a widget, in this case: the item labels
                for i in scroll_frame_children:
                    i.destroy()

                add_existing_tasks(scroll_frame,user_name)

# to clear all the items in the 2 do list
def clearAll(scroll_frame, userName):

    item_labels = scroll_frame.winfo_children()

    # destroying each label
    if item_labels is not None or item_labels != []:
        for i in item_labels:
            i.destroy()
    
    # opening the user's file and re-writing the updated info
    with open(f'files/users/{userName}.txt') as file:
        file = file.read()
        file = eval(file)
    pwd = file[userName]

    with open(f'files/users/{userName}.txt', 'w') as f:
        f.write(f'{{\'{userName}\':\'{pwd}\',\'rows\':1}}')
    