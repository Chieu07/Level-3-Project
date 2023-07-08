from tkinter import *
import tkinter as tk
import time

#log in page 

root = tk.Tk()
root.geometry("500x700+500+200")  #This is window size and the position of the window will pop up
root.resizable(False,False)       #This code makes the window size constant with able to adjust the window size 
root.title("To Do List App")

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


#Function 




update_time()
setup()
root.mainloop()
