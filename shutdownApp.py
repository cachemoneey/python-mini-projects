from tkinter import *
import os

root = Tk()
root.title("Shutdown App")
root.geometry("400x500")

def restartTime():
    os.system("shutdown /r /t 30")
    
def restart():
    os.system("shutdown /r /t 1")
    
def shutdown():
    os.system("shutdown /s /t 1")
    
def logout():
    os.system("shutdown -l")

# First button
restart_time_button = PhotoImage(file="")
first_button = Button(root, image=restart_time_button, borderwidth=0, cursor="hand2", command=restartTime)
first_button.place(x=10, y=10)

# Second button
close_button = PhotoImage(file="")
second_button = Button(root, image=close_button, borderwidth=0, cursor="hand2", command=root.destroy)
second_button.place(x=200, y=10)

# Third button
restart_button = PhotoImage(file="")
third_button = Button(root, image=restart_button, borderwidth=0, cursor="hand2", command=restart)
third_button.place(x=10, y=200)

# Fourth button
shutdown_button = PhotoImage(file="")
fourth_button = Button(root, image=shutdown_button, borderwidth=0, cursor="hand2", command=shutdown)
fourth_button.place(x=200, y=200)

# Fifth button
logout_button = PhotoImage(file="")
fifth_button = Button(root, image=logout_button, borderwidth=0, cursor="hand2", command=logout)
fifth_button.place(x=10, y=400)

root.mainloop()