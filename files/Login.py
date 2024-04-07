from PIL import Image
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from files import Todo
#from Run import Mainmenu

# function for checking whether there is already a user logged in
def check_loginStatus():
    with open("files/login_status.txt") as file:
        info = file.read()        
        if info == '':
            return 0
        else:
            info = eval(info)
            return info[0], info[1]

def logout(frame, mainmenu):
    with open("files/login_status.txt", 'w') as f:
        f.write('')
    mainmenu(frame)

#login function, passed as command to login button in run.py under mainmenu()
def login(root, user_name, pwd, mainmenu, frame = None):    

    # The file opening function is placed under try block incase the given usrname does not exist
    try:
            # file = open(f"files/users/{user_name}.txt", 'r+')     ############## debugging
        with open(f"files/users/{user_name}.txt", 'r+') as file:     
            user_info = file.read()
            user_info = eval(user_info)
            if user_info[user_name] == pwd:
                # print(pwd) ######################debugging
                if frame != None:
                    frame.destroy()

                with open("files/login_status.txt", 'w') as f:
                    f.write(str([user_name, pwd]))
                
                #----------------------------------frames-----------------------------------------
                #Setting up a new parent frame
                parent_frame = CTkFrame(root)
                parent_frame.place(relx = 0.5,rely = 0.5,relwidth = 1, relheight = 1, anchor = CENTER)

                parent_frame_bg=CTkImage(Image.open("images/img.jpg"), size = (900,650))
                parent_frame_bg_label=CTkLabel(parent_frame, image = parent_frame_bg)
                parent_frame_bg_label.place(relx = 0.5,rely = 0.5,relwidth = 1, relheight = 1, anchor = CENTER)

                #setting 2 child frames inside the parent_frame containing the UI components and 2do list repectively
                child_frame1 = CTkFrame(parent_frame, fg_color="#221a2e", border_color="#9e59f7", border_width=1, corner_radius=10)
                child_frame1.place(relx = 0.18, rely = 0.5, relwidth = 0.3, relheight = 0.85, anchor = CENTER)
                
                username_label = CTkLabel(child_frame1, text = "Current User:\n" + user_name, font = CTkFont(size = 20))
                username_label.place(relx = 0.5, rely = 0.08, anchor = CENTER)

                child_frame2 = CTkFrame(parent_frame, fg_color="#221a2e", border_color= "#9e59f7", border_width = 1, corner_radius= 10)
                child_frame2.place(relx = 0.67, rely = 0.5 ,relwidth = 0.6, relheight = 0.85 ,anchor = CENTER)

                # setting up a scrollframe inside the child frame2 that will hold the to do list
                scroll_frame = CTkScrollableFrame(child_frame2, fg_color = "#16101D")
                scroll_frame.place(relx = 0.5, rely = 0.45, relwidth= 0.9, relheight = 0.75, anchor = CENTER)
                
                print('ok1')
                #----------------Placing the existing notes/tasks in the scrollframe-----------------------
                Todo.add_existing_tasks(scroll_frame, user_name)
                #----------------Placing the existing notes/tasks in the scrollframe-----------------------
                print('ok2')

                # task label
                task_label = CTkLabel(child_frame2, text= "Task:", font= CTkFont(size = 14))
                task_label.place(relx = 0.15, rely = 0.88, anchor = CENTER)

                # entry for entering the items in the list
                list_entry = CTkEntry(child_frame2, placeholder_text="Enter task", height=35, corner_radius = 20)
                list_entry.place(relx = 0.55, rely = 0.88,relwidth = 0.7, anchor = CENTER )

                #--------------------------------buttons----------------------------------------

                # logout button
                logout_button_img = CTkImage(Image.open("images/logout_icon.png"), size=(40,40))
                logout_button = CTkButton(child_frame1, text = "   Logout   ", image = logout_button_img, fg_color="#16111F",hover_color="#49484a", width =85, height = 40, font=CTkFont(size=14), command = lambda : logout(parent_frame, mainmenu) )  # calls mainmenu function
                logout_button.place(relx = 0.5, rely = 0.2, anchor = CENTER)

                # Add button
                add_button_img = CTkImage(Image.open("images/add_icon.png"), size = (40,40))
                add_button = CTkButton(child_frame1, text = "     Add    ", image = add_button_img, font=CTkFont(size=14), fg_color= "#008836", hover_color="#006026", command = lambda : Todo.add_task(scroll_frame,list_entry, user_name))
                add_button.place(relx = 0.5, rely =0.77, anchor = CENTER)

                # delete button
                delete_button_img = CTkImage(Image.open("images/delete_icon.png"), size = (40,40))
                delete_button = CTkButton(child_frame1, text = "   Delete   ", image = delete_button_img,font=CTkFont(size=14), fg_color="#9E0000", hover_color="#7A0303", command = lambda : Todo.delete_task(scroll_frame,user_name))
                delete_button.place(relx = 0.5, rely = 0.9, anchor = CENTER)


            else:
                CTkMessagebox(icon = "cancel", title = "Error!", message="Incorrect password!")
                
    except:
        # if no user is found
        CTkMessagebox(icon = "cancel", title="Error!", message="No such username found!")