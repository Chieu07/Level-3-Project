from tkinter import *
import tkinter as tk
import time

#log in page 

root = tk.Tk()
root.geometry("500x500+450+50")  #This is window size and the position of the window will pop up
root.resizable(False,False)       #This code makes the window size constant with able to adjust the window size 
root.title("To Do List App")
Image_icon=PhotoImage(file="Image/task.png")
root.iconphoto(False, Image_icon)

task_list= []

def addtask(): 
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert ( END, task)

        

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete( ANCHOR)

def deleteAllTasks():
    global task_list
    task_list.clear()  # Clear the task list
    listbox.delete(0, END)  # Clear the listbox
    with open("tasklist.txt", "w") as taskfile:
        taskfile.write("") 

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

Button(root, text = "QUIT",bd =0, command= quit).pack(anchor=NW, padx=5, pady=5)


#Main 
frame= Frame(root, width =500, height=400, bg="#302f3a")
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
Button(root,image = Delete_icon, borderwidth=0,command = deleteTask).place(x=200, y=370, anchor=N)

#Delete all task button
Delete_all_icon = PhotoImage(file="/Users/chieutu/Documents/Project Image/delete4.png")
delete_all_button = Button(root, text="All", bg="#33333d",border=0, image=Delete_all_icon, compound="right", borderwidth=0, command=deleteAllTasks)
delete_all_button.place(x=300, y=370, anchor=N)
delete_all_button.bind("<Enter>", lambda event: delete_all_button.config(relief=SUNKEN))
delete_all_button.bind("<Leave>", lambda event: delete_all_button.config(relief=RAISED))


openTaskFile()

update_time()
setup()
root.mainloop()
