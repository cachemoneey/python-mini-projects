from tkinter import *

root = Tk()
root.title("Registration Form")
root.geometry("600x470")
root.resizable(False,False)

# Function to handle user registration
def register():
    name_info = nameValue.get()
    phone_info = phoneValue.get()
    gender_info = genderValue.get()
    email_info = emailValue.get()
    
    file = open(name_info + ".txt", "w")
    file.write(name_info + "\n")
    file.write(phone_info + "\n")
    file.write(gender_info + "\n")
    file.write(email_info + "\n")
    file.close()
    
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    genderEntry.delete(0, END)
    emailEntry.delete(0, END)
    
    Label(text="Registration success", fg="green", font=("Calibri")).place(x=250, y=430)

Label(root, text="Python Registration Form", font="Arial, 25").pack(pady=50)

Label(text="Name", font=23).place(x=100, y=150)
Label(text="Phone", font=23).place(x=100, y=200)
Label(text="Gender", font=23).place(x=100, y=250)
Label(text="Email", font=23).place(x=100, y=300)

# Entry
nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emailValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue, width=30, bd=2, font=20)
phoneEntry = Entry(root, textvariable=phoneValue, width=30, bd=2, font=20)
genderEntry = Entry(root, textvariable=genderValue, width=30, bd=2, font=20)
emailEntry = Entry(root, textvariable=emailValue, width=30, bd=2, font=20)

nameEntry.place(x=200, y=150)
phoneEntry.place(x=200, y=200)
genderEntry.place(x=200, y=250)
emailEntry.place(x=200, y=300)

# Check button
checkValue = IntVar
checkbtn = Checkbutton(text="Remember me?", variable=checkValue)
checkbtn.place(x=200, y=340)

Button(text="Register", font=20, width=11, height=2, command=register).place(x=250, y=380)

root.mainloop()
