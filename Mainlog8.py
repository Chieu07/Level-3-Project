from tkinter import * 
import tkinter as tk
import time
from tkinter import messagebox
import ast

# Login page window 
root = Tk()
root.title("Login")
root.geometry("925x500+150+100")
root.configure(bg="#f5f7fd")
root.resizable(False,False)

def signin():  #Function for login page
    username = user.get()
    password = code.get()

    file= open('datasheet.txt','r')   #The data will save and read in this file
    d= file.read()
    r=ast.literal_eval(d)
    file.close()

    print(r.keys())
    print(r.values())


    if username in r.keys() and password == r[username]: # If the password match with the file then it will create the main app window
        root.destroy()                                    
        main_win = tk.Tk()                    #This is the main window of the app
        main_win.geometry("500x500+150+100")  #This is window size and the position of the window will pop up
        main_win.resizable(False,False)       #This code makes the window size constant with able to adjust the window size 
        main_win.title("OSC Planner")
        Image_icon=PhotoImage(file="Image/task.png")
        main_win.iconphoto(False, Image_icon)

        task_list = []
        def addtask():      #Function of of the app, use list box to save the task and print out the list
            task = task_entry.get()
            task_entry.delete(0, END)

            if task:
                with open("tasklist.txt", 'a') as taskfile:
                    taskfile.write(f"\n{task}")
                task_list.append(task)
                listbox.insert ( END, task)
        
        def deleteTask(task):
            if task in task_list:
                task_list.remove(task)
                with open("tasklist.txt", 'w') as taskfile:
                    for task in task_list:
                        taskfile.write(task +"\n")
                listbox.delete( ANCHOR)
        
        def toggleTaskComplete(task_index):
            global task_list
            task_list[task_index] = f"[Done] {task_list[task_index]}"
            listbox.delete(task_index)
            listbox.insert(task_index, task_list[task_index])
                                 
                
        
        def openTaskFile(): 
            try:
                global task_list
                with open("tasklist.txt", "r") as taskfile:
                     tasks = taskfile.readlines()
    
                for task in tasks:
                 if task != '\n':
                    task_list.append(task)
                    listbox.insert(END, task)
            except:
                 file = open('tasklist.txt', 'w')
                 file.close()

        # Quit button
        def quit ():
            main_win.destroy()
        
        # LABEL AND BUTTON DECOR FOR THE MAIN APP BELOW 
        # Function to update time and dates 
        def update_time():
             current_time = time.strftime("%H:%M")
             current_date = time.strftime("%A-%d-%m-%Y")
             time_label.config(text=current_time)
             date_label.config(text=current_date)
             main_win.after(1000, update_time)
        
        # Create labels for dates and times
        date_label = tk.Label(main_win, font=("Roboto", 20),bg= "#302f3a",fg ='#FFFFFF')
        date_label.place(x=250, y=0, anchor = N)
        time_label = tk.Label(main_win, font=("Roboto", 20),bg= "#302f3a",fg ='#FFFFFF')
        time_label.place(x=435,y=0,) # Position the label at the top-right corner
        
        # Label and button
        def setup():
            main_win.config(bg="#302f3a")
            title =tk.Label(main_win,text= "What are you going to do? ", font=("Bebas Neue", 30, "bold"), bg="#302f3a", fg= '#89ddb3')
            title.place(x= 70, y = 40)

        Button(main_win, text = "QUIT",bd =0, command= quit).pack(anchor=NW, padx=5, pady=5)


         #Main- Create the frame for the main page 
        frame= Frame(main_win, width =500, height=400, bg="#302f3a")
        frame.place(x=0, y=100)
        task =StringVar()
        task_entry= Entry(frame, width=34, font="arial 20", bd=0)
        task_entry.place(x=0, y=0)
        task_entry.focus()

        button= Button(frame, text ="ADD",font="arial 20 bold", width=6, bg="#01f9b7", bd=10, command= addtask)
        button.place(x=419,y=1)

        #Listbox
        frame1 = Frame(frame,bd=2, width = 500, height=100, bg="#f0f0e9")
        frame1.place(x=0,y=32)

        listbox= Listbox(frame1, font=("arial", 12),width= 67, height= 15, bg="#f0f0e9", fg="Black", cursor= "hand2")
        listbox.pack(side=LEFT, fill= BOTH, padx =2 )
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side = RIGHT, fill= BOTH)

        listbox.config( yscrollcommand = scrollbar.set)
        scrollbar.config(command= listbox.yview)

        #Delete task button
        Delete_icon= PhotoImage(file="/Users/chieutu/Documents/Project Image/delete4.png")
        Button(main_win,image = Delete_icon, borderwidth= 0,command = lambda: deleteTask(str(listbox.get(ANCHOR)))).place(x=250, y=370, anchor=N)


        openTaskFile()

        update_time()
        setup()
        main_win.mainloop()
    else:                       #If the password in the login page does not match the file, then message box will pop up
        messagebox.showerror('Invalid',"invalid Username or Password")

###################################################################################################################################################
# This function to open the sign up page when click on the sign up button in the login page
def signup_command():
    root.destroy()       # The login page will be destroy if user clicked on the sign up button
    signup_win= Tk()            #Sign up page window 
    signup_win.title("Sign Up")
    signup_win.geometry("925x500+150+100")
    signup_win.configure(bg="#ffffff")
    signup_win.resizable(False,False)

    #Function for the sign up page 
    def sign_function ():          #This function will get the data of the user have inserted in the boxes.
        name= user_name.get()
        lastname= user_lastname.get()
        email = user_email.get()
        password= user_pass.get()
        password_confirm = user_confirmpass.get()

        if not name:
            messagebox.showerror("Error", "Please fill your Username.")
            Label(frame1, text="Require User name", fg="red", bg="#f5f7fd",font=("Arial", 10)).place(x=30, y=60)
            return
        
        if not lastname:
            messagebox.showerror("Error","Please fill your Last Name.")
            Label(frame1, text="Require Last name", fg="red", bg="#f5f7fd",font=("Arial", 10)).place(x=180, y=60)
            return
        
        if not email:
            messagebox.showerror("Error", "Please fill your Email")
            Label(signup_win, text="Require email", fg="red", bg="white",font=("Arial", 10)).place(x=830, y=215)
            return



        if password == password_confirm:   #If the password match then it will save in the file 
            try:
                file = open("datasheet.txt", "r+")  
                d = file.read()
                r=ast.literal_eval(d)

                dict2 ={name:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open("datasheet.txt","w")
                w = file.write(str(r))
                print("Password correct")
                messagebox.showinfo("Signup", "Successfully sign up")
            
            except: #If the file is not availible then it will create the own file to save the data 
                file = open("datasheet.txt", "w")
                pp = str({'Username':'Password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror("Invalid", "Both Password should match") #If the password not match with the confirm match, 
                                                                          # then message error pop up 


    
    #Set up the label and button for the sign up page here 
    img= PhotoImage(file="/Users/chieutu/Documents/Project Image/signup.png") 
    Label(signup_win,image=img, border=0, bg="white").place(x= 50, y= 90)

    frame1 = Frame(signup_win,width= 350, height= 340, bg="#f5f7fd")
    frame1.place(x=480, y=90)

    heading= Label(frame1, text="Sign up", bg="#f5f7fd", font=("Microsoft YaHei UI Light", 27, "bold"))
    heading.place(x=121, y=10)

    #Create the effect of the entry box function
    def on_enter(e): 
        user_name.delete(0, "end") #If the user click on the entry box, Username will delete 
    #def on_leave(e):
        #if user_name.get() == '':
            #user_name.insert(0,"User Name")  #If the user focus out the entry box then the username word will rewrite 
    user_name = Entry(frame1, width= 20, fg="black", border=0, bg="white", font =("Microsoft YaHei UI Light",11))
    user_name.place(x=30, y=80)
    user_name.insert(0,"User Name")
    user_name.bind("<FocusIn>",on_enter)
    #user_name.bind("<FocusOut>",on_leave)
    Frame(frame1, width= 148, height=2, bg="Black").place(x=31,y=102)

    def on_enter(e):
        user_lastname.delete(0, "end")
    #def on_leave(e):
        #if user_lastname.get() == '':
            #user_lastname.insert(0,"Last Name")

    user_lastname = Entry(frame1, width= 20, fg="black", border=0, bg="white", font =("Microsoft YaHei UI Light",11))
    user_lastname.place(x=180, y=80)
    user_lastname.insert(0,"Last Name")
    user_lastname.bind("<FocusIn>",on_enter)
    #user_lastname.bind("<FocusOut>",on_leave)
    Frame(frame1, width= 148, height=2, bg="Black").place(x=181,y=102)

    def on_enter(e):
        user_email.delete(0, "end")
   # def on_leave(e):
        #if user_email.get() == '':
           # user_email.insert(0,"Email")

    user_email = Entry(frame1, width= 42, fg="black", border=0, bg="white", font =("Microsoft YaHei UI Light",11))
    user_email.place(x=30, y=120)
    user_email.insert(0,"Email")
    user_email.bind("<FocusIn>",on_enter)
    #user_email.bind("<FocusOut>",on_leave)
    Frame(frame1, width= 300, height=2, bg="Black").place(x=31,y=140)

    def on_enter(e):
        user_pass.delete(0, "end")
    def on_leave(e):
        if user_pass.get() == '':
            user_pass.insert(0,"Password")

    user_pass = Entry(frame1, width= 42, fg="black", border=0, bg="white", font =("Microsoft YaHei UI Light",11))
    user_pass.place(x=30, y=160)
    user_pass.insert(0,"Password")
    user_pass.bind("<FocusIn>",on_enter)
    user_pass.bind("<FocusOut>",on_leave)
    Frame(frame1, width= 300, height=2, bg="Black").place(x=31,y=180)
    
    def on_enter(e):
        user_confirmpass.delete(0, "end")
    def on_leave(e):
        if user_confirmpass.get() == '':
            user_confirmpass.insert(0,"Confirm Password")

    user_confirmpass = Entry(frame1, width= 42, fg="black", border=0, bg="white", font =("Microsoft YaHei UI Light",11))
    user_confirmpass.place(x=30, y=200)
    user_confirmpass.insert(0,"Confirm Password")
    user_confirmpass.bind("<FocusIn>",on_enter)
    user_confirmpass.bind("<FocusOut>",on_leave)
    Frame(frame1, width= 300, height=2, bg="Black").place(x=31,y=220)

# Button 
    sign_button = Button(frame1, width= 15, pady= 7,text="Sign up", border= 0, bg="white", cursor="hand2",command=sign_function).place(x=100, y=250)
    
    ###################################################################################################################################################
    # Recreate the login page and function in the Sign Up page. If the user complete the sign up account,
    #then they can comeback to login the new account to access in the main app
    def resign():
        signup_win.destroy()        #Function to delete the sign up page if they click on the "Back" button 
        signin_two = Tk()           #Create the new window for login page        
        signin_two.title('Login')
        signin_two.geometry("925x500+150+100")
        signin_two.configure(bg="#f5f7fd")
        signin_two.resizable(False,False)
        
        def signin():
            username = user.get()
            password = code.get()

            file= open('datasheet.txt','r')
            d= file.read()
            r=ast.literal_eval(d)
            file.close()

            print(r.keys())
            print(r.values())

            # Planning page open 
            if username in r.keys() and password == r[username]:
                signin_two.destroy()
                main_win = tk.Tk()
                main_win.geometry("500x500+450+50")  #This is window size and the position of the window will pop up
                main_win.resizable(False,False)       #This code makes the window size constant with able to adjust the window size 
                main_win.title("OSC Planner")
                Image_icon=PhotoImage(file="Image/task.png")
                main_win.iconphoto(False, Image_icon)

                task_list = []

                def addtask():
                    task = task_entry.get()
                    task_entry.delete(0, END)

                    if task:
                        with open("tasklist.txt", 'a') as taskfile:
                            taskfile.write(f"\n{task}")
                        task_list.append(task)
                        listbox.insert ( END, task)

                def deleteTask(task):
                    if task in task_list:
                        task_list.remove(task)
                        with open("tasklist.txt", 'w') as taskfile:
                            for task in task_list:
                                taskfile.write(task +"\n")
                        
                        listbox.delete( ANCHOR)

                def toggleTaskComplete(task_index):
                    global task_list
                    task_list[task_index] = f"[Done] {task_list[task_index]}"
                    listbox.delete(task_index)
                    listbox.insert(task_index, task_list[task_index])


                def openTaskFile():
                    try:
                        global task_list
                        with open("tasklist.txt", "r") as taskfile:
                             tasks = taskfile.readlines()
    
                        for task in tasks:
                         if task != '\n':
                            task_list.append(task)
                            listbox.insert(END, task)
                    except:
                         file = open('tasklist.txt', 'w')
                         file.close()

                # Quit button
                def quit ():
                    main_win.destroy()

                # Function to update time and dates
                def update_time():
                     current_time = time.strftime("%H:%M")
                     current_date = time.strftime("%A-%d-%m-%Y")
                     time_label.config(text=current_time)
                     date_label.config(text=current_date)
                     main_win.after(1000, update_time)
        
                # Create labels for dates and times
                date_label = tk.Label(main_win, font=("Roboto", 20),bg= "#302f3a",fg ='#FFFFFF')
                date_label.place(x=250, y=0, anchor = N)
                time_label = tk.Label(main_win, font=("Roboto", 20),bg= "#302f3a",fg ='#FFFFFF')
                time_label.place(x=435,y=0,) # Position the label at the top-right corner
        
                # Label and button
                def setup():
                    main_win.config(bg="#302f3a")
                    title =tk.Label(main_win,text= "What are you going to do? ", font=("Bebas Neue", 30, "bold"), bg="#302f3a", fg= '#89ddb3')
                    title.place(x= 70, y = 40)

                Button(main_win, text = "QUIT",bd =0, command= quit).pack(anchor=NW, padx=5, pady=5)


                 #Main 
                frame= Frame(main_win, width =500, height=400, bg="#302f3a")
                frame.place(x=0, y=100)
                task =StringVar()
                task_entry= Entry(frame, width=34, font="arial 20", bd=0)
                task_entry.place(x=0, y=0)
                task_entry.focus()

                button= Button(frame, text ="ADD",font="arial 20 bold", width=6, bg="#01f9b7", bd=10, command= addtask)
                button.place(x=419,y=1)

                #Listbox
                frame1 = Frame(frame,bd=2, width = 500, height=100, bg="#f0f0e9")
                frame1.place(x=0,y=32)

                listbox= Listbox(frame1, font=("arial", 12),width= 67, height= 15, bg="#f0f0e9", fg="Black", cursor= "hand2")
                listbox.pack(side=LEFT, fill= BOTH, padx =2 )
                scrollbar = Scrollbar(frame1)
                scrollbar.pack(side = RIGHT, fill= BOTH)

                listbox.config( yscrollcommand = scrollbar.set)
                scrollbar.config(command= listbox.yview)

                #Delete task button
                Delete_icon= PhotoImage(file="/Users/chieutu/Documents/Project Image/delete4.png")
                Button(main_win,image = Delete_icon, borderwidth= 0,command = lambda: deleteTask(str(listbox.get(ANCHOR)))).place(x=250, y=370, anchor=N)
                

                openTaskFile()

                update_time()
                setup()
                main_win.mainloop()
            else:
                messagebox.showerror('Invalid',"invalid Username or Password")

        img = PhotoImage(file="/Users/chieutu/Documents/Project Image/planning3.png")
        Label(signin_two,image=img, bg='#f5f7fd').place(x=50,y=65)

        frame = Frame (signin_two, width = 350, height= 350, bg= "white")
        frame.place(x=480, y= 70)

        heading= Label(frame, text='Sign In', fg= "#57a1f8", bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
        heading.place(x = 130, y= 5)

        # User name Entry 
        def on_enter(e):
            user.delete(0,'end')

        def on_leave(e):
            name= user.get()
            if name=='':
                user.insert(0,'Username')
   
        user = Entry(frame, width=25, fg= "black", border=0, bg="white", font=("Microsoft YaHei UI Light",11))
        user.place(x= 30, y= 80)
        user. insert(0,"Username")
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)

        Frame(frame, width= 295, height=2, bg="black").place(x= 25, y=107)

        # User password entry 
        def on_enter(e):
            code.delete(0,'end')

        def on_leave(e):
            name= code.get()
            if name=='':
                code.insert(0,"Password")

        code = Entry(frame, width=25, fg= "black", border=0, bg="white", font=("Microsoft YaHei UI Light",11))
        code.place(x= 30, y= 150)
        code. insert(0,"Password")
        code.bind('<FocusIn>', on_enter)
        code.bind('<FocusOut>', on_leave)

        Frame(frame, width= 295, height=2, bg="black").place(x= 25, y=177)

        #Button
        Button(frame, width= 20, pady= 7, text="Sign in", bg="#57a1f8", fg="#57a1f8", border= 0,command= signin).place(x = 75, y=200)
        label =Label(frame, text="Don't have an account?", fg="black", bg="white",font=("Microsoft YaHei UI Light",9))
        label.place(x=75, y=270)

        sign_up= Button(frame,width= 6, text="Sign up", border= 0, bg="white", cursor="hand2", fg="#57a1f8",command=signup_command)
        sign_up.place(x=183, y= 267)

        signin_two.mainloop()
    
    back_button=Button(signup_win,text="Back",width=5, pady=3,command=resign).place(x=3, y=3)

    signup_win.mainloop()
    
################################################################################################################
 
 #Set up and decor for the Sign In page 
img = PhotoImage(file="/Users/chieutu/Documents/Project Image/planning3.png") #Upload the image on the window
Label(root,image=img, bg='#f5f7fd').place(x=50,y=65)

frame = Frame (root, width = 350, height= 350, bg= "white")
frame.place(x=480, y= 70)

heading= Label(frame, text='Sign In', fg= "#57a1f8", bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x = 130, y= 5)

# Function for Username Entry box
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name= user.get()
    if name=='':
        user.insert(0,'Username')
   
user = Entry(frame, width=25, fg= "black", border=0, bg="white", font=("Microsoft YaHei UI Light",11))
user.place(x= 30, y= 80)
user. insert(0,"Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width= 295, height=2, bg="black").place(x= 25, y=107)

# Function for the user password entry box
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name= code.get()
    if name=='':
        code.insert(0,"Password")

code = Entry(frame, width=25, fg= "black", border=0, bg="white", font=("Microsoft YaHei UI Light",11))
code.place(x= 30, y= 150)
code. insert(0,"Password")
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width= 295, height=2, bg="black").place(x= 25, y=177)

#Button
Button(frame, width= 20, pady= 7, text="Sign in", bg="#57a1f8", fg="#57a1f8", border= 0,command= signin).place(x = 75, y=200)
label =Label(frame, text="Don't have an account?", fg="black", bg="white",font=("Microsoft YaHei UI Light",9))
label.place(x=75, y=270)

sign_up= Button(frame,width= 6, text="Sign up", border= 0, bg="white", cursor="hand2", fg="#57a1f8",command=signup_command)
sign_up.place(x=183, y= 267)

root.mainloop()
