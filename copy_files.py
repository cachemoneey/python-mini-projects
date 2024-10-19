import time
import shutil
import os

path = "C:\\Users\\azizurrohman\\Desktop"
os.chdir(path)

def copy_files():
    file = input("Enter file to copy: ")
    new_dir = input("Enter DIR name: ")
    
    shutil.copy(file, new_dir)
    print("File copying...")
    time.sleep(1)
    list_dir = os.listdir(new_dir)
    print("Contents are: ", list_dir)
    print("Deleting old file on desktop...")
    time.sleep(1)
    clean_file = "C:\\Users\\azizurrohman\\Desktop\\new.txt"
    os.remove(clean_file)
    print("Old file has been deleted.")
    
copy_files()