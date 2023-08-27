from tkinter import * 
from tkinter import messagebox

root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file="/Users/chieutu/Documents/Project Image/login.png")
Label(root,image=img, bg='White').place(x=50,y=50)

frame = Frame (root, width = 350, height= 350, bg= "white")
frame.place(x=480, y= 70)

heading= Label(frame, text='Sign In', fg= "#57a1f8", bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x = 100, y= 5)

# User Entry 
user = Entry(frame, width=25, fg= "black", border=0, bg="white", font=("Microsoft YaHei UI Light",11))
user.place(x= 30, y= 80)
user. insert(0,"Username")

Frame(frame, width= 295, height=2, bg="black").place(x= 25, y=107)

######
code = Entry(frame, width=25, fg= "black", border=0, bg="white", font=("Microsoft YaHei UI Light",11))
code.place(x= 30, y= 150)
code. insert(0,"Password")

Frame(frame, width= 295, height=2, bg="black").place(x= 25, y=177)

#Button
Button(frame, width= 20, pady= 7, text="Sign in", bg="#57a1f8", fg="#57a1f8", border= 0).place(x = 75, y=200)
label =Label(frame, text="Don't have an account?", fg="black", bg="white",font=("Microsoft YaHei UI Light",9))
label.place(x=75, y=270)

sign_up= Button(frame,width= 6, text="Sign up", border= 0, bg="white", fg="#57a1f8")
sign_up.place(x=75, y= 270)

root.mainloop()
