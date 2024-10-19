# pip/3 install pwinput

import time
import os 
import pwinput

my_password = ["open_explorer123"]

def open_explorer():
    pw = pwinput.pwinput(prompt="Enter Password: ", mask="*")
    if(pw in my_password):
        print("Opening,,,")
        time.sleep(1)
        open_window()
    else:
        print("Passowrd is wrong. Try again!")
    
def open_window():
    os.startfile('explorer.exe')

open_explorer()