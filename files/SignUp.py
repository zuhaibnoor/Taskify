from customtkinter import *
from CTkMessagebox import CTkMessagebox
from PIL import Image

# takes up root window, the previous frame and the previous home menu to go back to it
def signUp(root_win=None,frame=None, menu=None):          

     # this function handles the creation of user accounts
     # passed to signup button as command        
    def create_account(name,pwd,co_pwd):       
        username = name.get()
        pswd = pwd.get()
        confirm_pwd = co_pwd.get()

        if pswd != confirm_pwd:
                CTkMessagebox(message="The passwords do not match. Make sure the password and confirm password have same passwords.", title = "Error", icon = "cancel")
                co_pwd.delete(0,END)
        else:    
                try:    
                        file = open(f"files/users/{username}.txt")
                        CTkMessagebox(message=f"The username \' {username} \' you entered is already taken. Try again with a different one.", title = "Error", icon = "cancel", button_color="#9e59f7", button_hover_color="#7330c9")
                except:
                        if name.get() == '' or pwd.get() == '' or co_pwd.get() == '':
                               CTkMessagebox(message="Error! Empty fields.", title = "Error", icon = "cancel",button_color="#9e59f7",button_hover_color="#7330c9" )
                        else:
                                user_info = str({username:pswd})
                                with open(f"files/users/{username}.txt","w") as user_file:
                                        user_file.write(user_info)
                                CTkMessagebox(message=f"Your account with username '{username}' has been successully created.", title = "Signup Successful!", icon = "check",button_color="#9e59f7",button_hover_color= "#7330c9")    
                                name.delete(0,END)
                                pwd.delete(0,END)
                                co_pwd.delete(0,END)
            
    
    #---------------------------------------SignUp fuction------------------------------------------
    if frame != None:
        frame.destroy() #will delete the signin frame passed to the function arguments to load new interface
    

    #setting up a main frame
    main_frame = CTkFrame(root_win)
    main_frame.place(relx = 0.5,rely = 0.5,relwidth = 1, relheight = 1, anchor = CENTER)

    #setting up the background of a mainframe
    main_frame_bg=CTkImage(Image.open("images/img.jpg"), size = (900,650))
    main_frame_bg_label=CTkLabel(main_frame, image = main_frame_bg)
    main_frame_bg_label.place(relx = 0.5,rely = 0.5,relwidth = 1, relheight = 1, anchor = CENTER)


    # setting up the signup frame
    signup_frame = CTkFrame(root_win,fg_color="#221a2e", border_color="white", border_width=1, corner_radius=10)   
    signup_frame.place(relx = 0.5, rely = 0.5, relwidth = 0.4, relheight = 0.8, anchor = CENTER)

    avatar_img = CTkImage(Image.open("images/avatar.png"), size = (80,80) )      #avatar image object
    avatar_img_label = CTkLabel(signup_frame, image = avatar_img, text = "")
    avatar_img_label.place(relx=0.37, rely = 0.1, anchor = CENTER)
    
    signin_heading = CTkLabel(signup_frame,text ="SignUp",font = CTkFont(size = 25, weight = "bold"))
    signin_heading.place(relx = 0.57, rely = 0.1, anchor = CENTER)


    #------------------- input labels and entries------------------
    username_label = CTkLabel(signup_frame, text="Username", font = CTkFont(size = 15))
    username_label.place(relx = 0.2, rely = 0.27, anchor = CENTER)

    username_entry = CTkEntry(signup_frame, placeholder_text="Enter your username", height=35, corner_radius = 20)
    username_entry.place(relx = 0.5, rely = 0.33,relwidth = 0.7, anchor = CENTER )

    password_label = CTkLabel(signup_frame, text="Password", font = CTkFont(size = 15))
    password_label.place(relx = 0.2, rely = 0.43, anchor = CENTER)

    password_entry = CTkEntry(signup_frame, placeholder_text="Enter your password", height=35, corner_radius=20)
    password_entry.place(relx = 0.5, rely = 0.49,relwidth = 0.7, anchor = CENTER )

    confirm_password_label = CTkLabel(signup_frame, text="Confirm Password", font = CTkFont(size = 15))
    confirm_password_label.place(relx = 0.28, rely = 0.59, anchor = CENTER)

    confirm_password_entry = CTkEntry(signup_frame, placeholder_text="Confirm your password", height=35, corner_radius=20)
    confirm_password_entry.place(relx = 0.5, rely = 0.65,relwidth = 0.7, anchor = CENTER )
    
       
    #---------------------signup and back buttons-------------------------

            #signUp button
    Signup_button = CTkButton(signup_frame, text="Signup",font = CTkFont(size =14),width = 200 ,height=40,corner_radius=20, fg_color="#9e59f7", text_color="black", hover_color="#7330c9", command = lambda : create_account(username_entry, password_entry, confirm_password_entry))
    Signup_button.place(relx=0.5,rely=0.9, anchor = CENTER)

            #back button

    img = CTkImage(Image.open("images/back_icon.png"), size=(40,40))
    back_button = CTkButton(signup_frame, text = "", image = img, fg_color=signup_frame._fg_color,hover_color="#49484a",command = lambda : menu(main_frame), width =20, height = 40)
    back_button.place(relx = 0.07, rely = 0.05)

   


    