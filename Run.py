from customtkinter import *
from PIL import Image
from files import SignUp, Login



#----------------setting up the root window-----------------------------
root = CTk()

# setting the dimensions of the window and the coordinates at which it should appear
root.geometry("900x650+0+100")

# disabling the resizing option on top of the window
root.resizable(False,False)

# title of the application
root.title("2 DO")

# theme
set_appearance_mode("dark")

#----------------setting up the root window-----------------------------


# ---------------------------the mainmenu-----------------------------
def Mainmenu(frame=None):
    
    # check_loginStatus() function checks if there is a user currently logged in to the application
    # returns zero if there is no user logged in
    current_user_info = Login.check_loginStatus()
    

    if current_user_info == 0:
        if frame != None:
            frame.destroy()

        #----------------------setting up a main frame------------------------------
        main_frame = CTkFrame(root)
        main_frame.place(relx = 0.5,rely = 0.5,relwidth = 1, relheight = 1, anchor = CENTER)

        #setting up the background of a mainframe
        main_frame_bg=CTkImage(Image.open("images/img.jpg"), size = (900,650))
        main_frame_bg_label=CTkLabel(main_frame, image = main_frame_bg)
        main_frame_bg_label.place(relx = 0.5,rely = 0.5,relwidth = 1, relheight = 1, anchor = CENTER)

        welcome = CTkLabel(main_frame, text="WELCOME", font =  CTkFont(size=40, weight="bold",family="courier new"),corner_radius=10, bg_color="#221a2e")
        welcome.place(relx = 0.5,rely = 0.15, anchor = CENTER)

        #------------------------setting the signin frame--------------------------------
        signin_frame = CTkFrame(main_frame, fg_color="#221a2e", border_color="white", border_width=1, corner_radius=10)
        signin_frame.place(relx = 0.5, rely = 0.6, relwidth = 0.4, relheight = 0.7, anchor = CENTER)

        avatar_img = CTkImage(Image.open("images/avatar.png"), size = (80,80) )      #avatar image object
        avatar_img_label = CTkLabel(signin_frame, image = avatar_img, text = "")
        avatar_img_label.place(relx=0.37, rely = 0.1, anchor = CENTER)

        signin_heading = CTkLabel(signin_frame,text ="SignIn",font = CTkFont(size = 25, weight = "bold"))
        signin_heading.place(relx = 0.57, rely = 0.1, anchor = CENTER)
        
        #------------------------inputs and labels-------------------------------

        username_label = CTkLabel(signin_frame, text="Username", font = CTkFont(size = 15))
        username_label.place(relx = 0.2, rely = 0.25, anchor = CENTER)

        username_entry = CTkEntry(signin_frame, placeholder_text="Enter your username", height=35, corner_radius = 20)
        username_entry.place(relx = 0.5, rely = 0.33,relwidth = 0.7, anchor = CENTER )

        password_label = CTkLabel(signin_frame, text="Password", font = CTkFont(size = 15))
        password_label.place(relx = 0.2, rely = 0.41, anchor = CENTER)

        password_entry = CTkEntry(signin_frame, placeholder_text="Enter your password", height=35, corner_radius=20, show = "*")
        password_entry.place(relx = 0.5, rely = 0.49,relwidth = 0.7, anchor = CENTER )


        #--------------------------buttons-------------------------------------------

        #login button
        login_button = CTkButton(signin_frame, text="Login",font = CTkFont(size =14),width = 200 , height=40,corner_radius=20, fg_color="#9e59f7", text_color="black", hover_color="#7330c9", command = lambda: Login.login(root, username_entry.get(), password_entry.get(), Mainmenu, main_frame))
        login_button.place(relx=0.5,rely=0.65, anchor = CENTER)

        # // horizontal rule
        hr = CTkLabel(signin_frame,text="__________________________________________________",text_color="white")
        hr.place(relx = 0.5,rely = 0.75, anchor = CENTER)

        label = CTkLabel(signin_frame, text="Don't have an account or want more accounts?\nClick SignUp now!", font= CTkFont(size=14))
        label.place(relx = 0.5, rely = 0.83,anchor = CENTER )

        # signup button
        Signup_button = CTkButton(main_frame, text="SignUp",font = CTkFont(size =14),width = 200 ,height=40,corner_radius=20, fg_color="#9e59f7", bg_color="#221a2e", text_color="black", hover_color="#7330c9", command = lambda : SignUp.signUp(root,main_frame, Mainmenu))
        Signup_button.place(relx=0.5,rely=0.9, anchor = CENTER)

    else:
        Login.login(root, current_user_info[0], current_user_info[1], Mainmenu)

Mainmenu()

root.mainloop()