from customtkinter import *
from CTkMessagebox import CTkMessagebox


def create_label(frame, task, row):
    print("in CL 1") ################ debugging
    parent_frame = CTkFrame(frame,
                            fg_color="#2C2435",
                            border_color = "white")
    parent_frame.grid(row = row, column = 0, padx = 10, pady = 10)
    print("in CL 2") ################ debugging
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

            #------------creating a label for the new task and placing it in a grid------------
            # task_label = CTkLabel(scroll_frame, text= f'{user_info["rows"]} : {task}')
            #  # The "rows" stored in the file start from 1, therefore for customtkinter, we have done- 
            #  # user_info["rows"]-1 because we have to provide rows that start from 0 for it to be placed
            # task_label.grid(row = user_info['rows']-1, column = 0 )
            create_label(scroll_frame,task, user_info['rows']-1)

            
            print(user_info['rows'])    ######debugging
            

            #------saving the task in the user_info dictionary----------
            user_info[user_info['rows']-1] = task
            user_info['rows'] += 1

            #----writing the new task added by the user in the file----
            with open(f'files/users/{UserName}.txt', 'w') as f:
                f.write(str(user_info))

    entry.delete(0,END)


#function for adding existing tasks on the scrollframe
def add_existing_tasks(scrl_frm, UserName):
    print("in AET 1") ################ debugging
    with open(f'files/users/{UserName}.txt') as f:
        user_info = f.read()
        user_info = eval(user_info)
        
        print("in AET 2") ################ debugging
        
        #removing the unnecessary info from the user_info
        user_info.pop(UserName)
        user_info.pop('rows')

        if user_info != {}:
            rows = 1

            for i in user_info:
                print("in AET 3") ################ debugging
                # placing each task on the scrollframe saved in the file
                # task_label = CTkLabel(scrl_frm, text= f'{rows} : {user_info[i]}')
                # task_label.grid(row = i, column = 0)
                create_label(scrl_frm, user_info[i], i)
                rows += 1 

def delete_task(scroll_frame, user_name):

    popup = CTkInputDialog(text = "Delete item No.",
                           button_fg_color="#9E0000",
                           button_hover_color="#7A0303")    
    task_no = popup.get_input()

    if task_no != user_name and task_no != 'rows':
        print(task_no)
        task_no = (int(task_no)) - 1
        with open(f'files/users/{user_name}.txt') as f:
            f = f.read()
            user_info = eval(f)
            # print(type(user_info)) ################## debugging
            user_pwd = user_info.pop(user_name)
            rows = (user_info.pop("rows")) - 1
            if task_no in user_info:
                user_info.pop(task_no)
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
                print(new_user_info)

                with open(f'files/users/{user_name}.txt', 'w') as file:
                    file.write(str(new_user_info))
                    scroll_frame_children = scroll_frame.winfo_children()
                    for i in scroll_frame_children:
                        i.destroy()
                add_existing_tasks(scroll_frame,user_name)


# root = CTk()
# root.geometry("300x300")

# create_label(root, "abcdef", 1)
# root.mainloop()
                



