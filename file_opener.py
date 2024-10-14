import os
from PIL import Image
import webbrowser
import time

def open_files():
    print("===================")
    print("Choose file to open")
    print("===================")
    path = "C:\\Users\\azizurrohman\\Desktop"
    os.chdir(path)
    list_dir = os.listdir(path)
    print("Files are: ", list_dir)
    
    filename = input("Enter full filename: ")
    if filename.endswith(".txt"):
        with open(filename, "r") as file_object:
            contents = file_object.read()
            print(contents)
    elif filename.endswith(".docx"):
        os.system(f"start {filename}")
    elif filename.endswith(".jpg"):
        image = Image.open(filename)
        image.show()
    else:
        print("Unknown format.")
        file_help()

def file_help():
    time.sleep(1)
    webbrowser.open("https://en.wikipedia.org/wiki/List_of_file_formats")
    
open_files()