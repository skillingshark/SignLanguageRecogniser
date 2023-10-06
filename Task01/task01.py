# %%
from tkinter import * # tkinter is a standard GUI library
import tkinter.messagebox # messagebox widget to display messages 
from plyer import notification
import time
import schedule

# %%
window=Tk() # creates a main application window 
window.title("To-Do List App") # title to be displayed at the top

# %%
frame_task=Frame(window) # frame widget to hold the listbox and scrollbar 
                         # Frame() - container widget within the main window (which is taken as argument)
frame_task.pack() # pack() - organises the widget before placing it in the main window

# %%
listbox_task=Listbox(frame_task, bg="black", fg="white", height=15, width=50,font="Helvetica")
# Listbox() - stores all the tasks that we list 
listbox_task.pack(side=tkinter.LEFT)

# %%
scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

# %%
listbox_task.config(yscrollcommand=scrollbar_task.set) # setting scrollbar to listbox_task widget
scrollbar_task.config(command=listbox_task.yview) # configuring it on vertical axis

# %%
def entertask():
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            listbox_task.insert(END, input_text)
            root1.destroy()
    
    def time_entry():
        root2=Tk()
        root2.title("Set Time")
        time=0
        def exit():     
            time=float(entry_time.get(1.0, "end-1c"))
            root2.destroy()      
            schedule.every(time).minutes.do(notification.notify(
            title="Task",
            message=input_text,
            timeout=10
            )  ) 
        entry_time=Text(root2, width=20, height=4)
        entry_time.pack()
        button_ok=Button(root2, text="OK", command=exit)
        button_ok.pack()
        
    root1=Tk()
    root1.title("Add task")
    entry_task=Text(root1, width=40, height=4)
    entry_task.pack()
    button_reminder=Button(root1, text="Set Reminder Time",command=time_entry)
    button_reminder.pack()
    button_temp=Button(root1, text="Add task", command=add)
    button_temp.pack()
    root1.mainloop()

# %%
def deletetask():
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0])

# %%
def markcompleted():
    marked=listbox_task.curselection()
    temp=marked[0]
    temp_marked=listbox_task.get(marked)
    temp_marked=temp_marked+" ✔"
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)

# %%
entry_button=Button(window, text="Add task", width=50, command=entertask)
entry_button.pack(pady=3)

# %%
delete_button=Button(window, text="Delete selected task", width=50, command=deletetask)
delete_button.pack(pady=3)

# %%
mark_button=Button(window, text="Mark as completed", width=50, command=markcompleted)
mark_button.pack(pady=3)

# %%
window.mainloop()


