import os
import shutil
import time

def create_folder():
    path = "C:\\Users\\azizurrohman\\Desktop"
    os.chdir(path)
    print("Creating file...")
    time.sleep(1)
    os.mkdir("new_folder")
    print("New directory created.")
    
def create_file():
    path = "C:\\Users\\azizurrohman\\Desktop"
    os.chdir(path)
    with open("new_file.txt", "w") as file_object:
        file_object.write("New file created.")
        
def rename_file():
    path = "C:\\Users\\azizurrohman\\Desktop"
    os.chdir(path)
    old_name = input(("Enter old name: "))
    new_name = input(("Enter new name: "))
    os.rename(old_name, new_name)
    
def copy_file():
    path = "C:\\Users\\azizurrohman\\Desktop"
    os.chdir(path)
    path2 = "C:\\Users\\azizurrohman\\Desktop\\new_folder"
    file_name = input("Enter file to copy: ")
    if os.path.exists(file_name):
        shutil.copy(file_name, path2)
        print("File copied!")
    else:
        print("An error occurred.")
        
create_folder()
create_file()
rename_file()
copy_file()