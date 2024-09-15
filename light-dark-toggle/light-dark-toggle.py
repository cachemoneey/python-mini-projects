from tkinter import *

root = Tk()
root.title("Toggle Switch")
root.geometry("400x600")
root.configure(bg="white")
root.resizable(False, False)

# Copy from here to any other programme
#####################################################################

button_mode = True

def customize():
    
    global button_mode
    
    if button_mode:
        button.config(image=off, bg="#26242f", activebackground="#26242f")
        root.config(bg="#26242f")
        button_mode=False
    else:
        button.config(image=on, bg="white", activebackground="white")
        root.config("white")
        button_mode=True

on = PhotoImage(file="light.png")
off = PhotoImage(file="dark.png")

button = Button(root, image=on, bd=0, bg="white", activebackground="white", command=customize)
button.pack(padx=50, pady=50)

#####################################################################

root.mainloop()