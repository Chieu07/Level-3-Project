from tkinter import *
import tkinter as tk
import time

#log in page 

root = tk.Tk()
root.geometry("500x600+450+50")  #This is window size and the position of the window will pop up
root.resizable(False,False)       #This code makes the window size constant with able to adjust the window size 
root.title("To Do List App")
Image_icon=PhotoImage(file="Image/task.png")
root.iconphoto(False, Image_icon)



# Quit button
def quit ():
    root.destroy()



# Function to update time and dates
def update_time():
    current_time = time.strftime("%H:%M")
    current_date = time.strftime("%A-%d-%m-%Y")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)

# Create labels for dates and times
date_label = tk.Label(root, font=("Roboto", 20),bg= "#302f3a",fg ='#FFFFFF')
date_label.place(x=250, y=0, anchor = N)
time_label = tk.Label(root, font=("Roboto", 20),bg= "#302f3a",fg ='#FFFFFF')
time_label.place(x=435,y=0,) # Position the label at the top-right corner

# Label and button
def setup():
    root.config(bg="#302f3a")
    title =tk.Label(root,text= "What are you going to do? ", font=("Bebas Neue", 30, "bold"), bg="#302f3a", fg= '#89ddb3')
    title.place(x= 70, y = 40)

Button(root, text = "QUIT", command= quit).grid(row = 0, column= 0, sticky  =E) 


#Main 
frame= Frame(root, width =500, height=400, bg="#302f3a")
frame.place(x=0, y=100)

task =StringVar()
task_entry= Entry(frame, width=34, font="arial 20", bd=0)
task_entry.place(x=0, y=0)
task_entry.focus()

button= Button(frame, text ="ADD",font="arial 20 bold", width=6, bg="#01f9b7", bd=10)
button.place(x=419,y=1)

#Listbox
frame1 = Frame(frame,bd=3, width = 700, height=400, bg="#f0f0e9")
frame1.place(x=0,y=32)

update_time()
setup()
root.mainloop()

