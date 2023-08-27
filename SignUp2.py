from tkinter import * 
from tkinter import messagebox
import ast

root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#f5f7fd")
root.resizable(False,False)

########### New Page connect- Sign Up page #############################################

def signup_page():
    root.destroy()

    signup = Tk()
    signup.title("Login")
    signup.geometry("925x500+300+200")
    signup.configure(bg="#ffffff")
    signup.resizable(False,False)

    def sign_function ():
        name= user_name.get()
        lastname= user_lastname.get()
        password= user_pass.get()
        password_confirm = user_confirmpass.get()

        if password == password_confirm:
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
            
            except:
                file = open("datasheet.txt", "w")
                pp = str({'Username':'Password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror("Invalid", "Both Password should match")
    
    img= PhotoImage(file="/Users/chieutu/Documents/Project Image/signup.png")
    Label(signup,image=img, border=0, bg="white").place(x= 50, y= 90)

    frame1 = Frame(signup,width= 350, height= 340, bg="#f5f7fd")
    frame1.place(x=480, y=90)

    heading= Label(frame1, text="Sign up", bg="#f5f7fd", font=("Microsoft YaHei UI Light", 27, "bold"))
    heading.place(x=121, y=10)

    def on_enter(e):
        user_name.delete(0, "end")
    def on_leave(e):
        if user_name.get() == '':
            user_name.insert(0,"First Name")
    user_name = Entry(frame1, width= 20, fg="black", border=0, bg="white", font =("Microsoft YaHei UI Light",11))
    user_name.place(x=30, y=80)
    user_name.insert(0,"First Name")
    user_name.bind("<FocusIn>",on_enter)
    user_name.bind("<FocusOut>",on_leave)
    Frame(frame1, width= 148, height=2, bg="Black").place(x=31,y=102)

    def on_enter(e):
        user_lastname.delete(0, "end")
    def on_leave(e):
        if user_lastname.get() == '':
            user_lastname.insert(0,"Last Name")

    user_lastname = Entry(frame1, width= 20, fg="black", border=0, bg="white", font =("Microsoft YaHei UI Light",11))
    user_lastname.place(x=180, y=80)
    user_lastname.insert(0,"Last Name")
    user_lastname.bind("<FocusIn>",on_enter)
    user_lastname.bind("<FocusOut>",on_leave)
    Frame(frame1, width= 148, height=2, bg="Black").place(x=181,y=102)

    def on_enter(e):
        user_email.delete(0, "end")
    def on_leave(e):
        if user_email.get() == '':
            user_email.insert(0,"Email")

    user_email = Entry(frame1, width= 42, fg="black", border=0, bg="white", font =("Microsoft YaHei UI Light",11))
    user_email.place(x=30, y=120)
    user_email.insert(0,"Email")
    user_email.bind("<FocusIn>",on_enter)
    user_email.bind("<FocusOut>",on_leave)
    Frame(frame1, width= 300, height=2, bg="Black").place(x=31,y=140)

    def on_enter(e):
        user_pass.delete(0, "end")
    def on_leave(e):
        if user_pass.get() == '':
            user_pass.insert(0,"Pass Word")

    user_pass = Entry(frame1, width= 42, fg="black", border=0, bg="white", font =("Microsoft YaHei UI Light",11))
    user_pass.place(x=30, y=160)
    user_pass.insert(0,"Pass Word")
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
    user_confirmpass.insert(0,"Confirm Pass Word")
    user_confirmpass.bind("<FocusIn>",on_enter)
    user_confirmpass.bind("<FocusOut>",on_leave)
    Frame(frame1, width= 300, height=2, bg="Black").place(x=31,y=220)

# Button 
    sign_button = Button(frame1, width= 15, pady= 7,text="Sign up", border= 0, bg="white", cursor="hand2",command=sign_function).place(x=100, y=250)
     

    signup.mainloop()
    
##################################################################################################

def signin():
    username = user.get()
    password = code.get()

    if username == "admin" and password == "1234":
        print("correct account")
        #add the main page here
    
    elif username != 'admin' and password != '1234':
        messagebox. showerror("invalid", "Invalid username or Password")
    
    elif password != '1234':
        messagebox. showerror("invalid", "Invalid Password")
    
    elif username != 'admin':
        messagebox. showerror("invalid", "Invalid username")
    
   
img = PhotoImage(file="/Users/chieutu/Documents/Project Image/planning3.png")
Label(root,image=img, bg='#f5f7fd').place(x=50,y=65)

frame = Frame (root, width = 350, height= 350, bg= "white")
frame.place(x=480, y= 70)

heading= Label(frame, text='Sign In', fg= "#57a1f8", bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x = 100, y= 5)

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
        code.insert(0,'Password')

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

sign_up= Button(frame,width= 6, text="Sign up", border= 0, bg="white", cursor="hand2", fg="#57a1f8",command=signup_page)
sign_up.place(x=183, y= 267)


root.mainloop()
