from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfFileWriter, PdfFileReader # pip install PyPDF2

import os

root = Tk()
root.title("PDF Protector")
root.geometry("400x400")
root.resizable(True, True)

def browse():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select Image File",
                                          filetypes=(('PDF File','*.pdf'),('all files','*.*')))
    entry1.insert(END, filename)
    
def Protect():
    mainfile = source.get()
    protectfile = target.get()
    code = password.get()
    
    if mainfile == "" and protectfile == "" and password.get() == "":
        messagebox.showerror("Invalid", "All entries are empty.")
    
    elif mainfile == "":
        messagebox.showerror("Invalid", "Please type source PDF filename.")
    
    elif protectfile == "":
        messagebox.showerror("Invalid", "Please type target PDF filename.")
    
    elif password.get() == "":
        messagebox.showerror("Invalid", "Please type password.")
        
    else:
        try:
            out = PdfFileWriter()
            file = PdfFileReader(filename)
            num = file.numPages
            
            for idx in range(num):
                page = file.getPage(idx)
                out.addPage(page)
                
            # password
            out.encrypt(code)
            
            with open(protectfile, "wb") as f:
                out.write(f)
                
            source.set("")
            target.set("")
            password.set("")
            
            messagebox.showerror("Info","Succesfully done!")
            
        except:
            messagebox.showerror("Invalid","Invalid entry.")
            
    
# icon
# choose your icon
image_icon = PhotoImage(file="")
root.iconphoto(False, image_icon)

# main
Top_image = PhotoImage(file="")
Label(root, image=Top_image).pack()

frame = Frame(root, width=580, height=290, bd=5, relief=GROOVE)
frame.place(x=10, y=130)

####################
source = StringVar()
Label(frame, text="Source PDF File:", font="Arial 10 bold", fg="#4c4542").place(x=30, y=50)
entry1 = Entry(frame, width=30, textvariable=source, font="Arial 15", bd=1)
entry1.place(x=150, y=48)

Button_icon = PhotoImage(file="")
Button(frame, image=Button_icon, width=35, height=24, bg="#d3cdcd", command=browse).place(x=500, y=47)

####################
target = StringVar()
Label(frame, text="Target PDF File:", font="Arial 10 bold", fg="#4c4542").place(x=30, y=100)
entry2 = Entry(frame, width=30, textvariable=target, font="Arial 15", bd=1)
entry2.place(x=150, y=100)

####################
password = StringVar()
Label(frame, text="Set User Password:", font="Arial 10 bold", fg="#4c4542").place(x=15, y=150)
entry3 = Entry(frame, width=30, textvariable=password, font="Arial 15", bd=1)
entry3.place(x=150, y=150)

button_icon = PhotoImage(file="")
Protect = Button(root, text="Protect PDF File", compound=LEFT, image=button_icon, width=230, height=50, bg="#bfb9b9", font="Arial 14 bold", command=Protect)
Protect.pack(side=BOTTOM, pady=40)

root.mainloop()