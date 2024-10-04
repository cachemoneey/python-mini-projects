import os
import pwinput

def enter_password():
    password = "abc123"
    pw = pwinput.pwinput(prompt="Enter password: ", mask="*")
    if pw == password:
        print("Password is correct")
        open_apps()
    else:
        print("Password is incorrect. Try again.")
        enter_password()
        
def open_apps():
    run = input("Choose an app: (1)Calculator (2)Notepad (3)MSPaint or exit? ")
    if run == "1":
        os.system("calc.exe")
    elif run == "2":
        os.system("notepad.exe")
    elif run == "3":
        os.system("mspaint.exe")
    elif run.lower() == "exit":
        print("Goodbye!")
        quit()
    else:
        print("An error has occurred.")

enter_password()