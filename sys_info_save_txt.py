import os
import time

def create_dir():
    path = "C:\\Users\\azizurrohman\\Desktop"
    os.chdir(path)
    print("Creating directory...")
    time.sleep(1)
    os.mkdir("windowsinfo")
    print("Created file on desktop")
    control()

def control():
    print("1.systeminfo 2.Exit")
    entry = input("Ente option: ")
    if (entry == "1"):
        print("Please wait...")
        get_system_info()
    else:
        quit_program()
        
def get_system_info():
    path = "C:\\Users\\azizurrohman\\Desktop\\windowsinfo"
    os.chdir(path)
    result = os.popen('systeminfo').read()
    with open("systeminfo.txt", "w") as file_object:
        file_object.write(result)
        print("File created in deirectory!")
        
def quit_program():
    print("Bye!")
    quit()
    
create_dir()