import os
import time

def get_size():
    path = "C\\Users\\azizurrohman\\Desktop" # choose the file path for your file
    os.chdir(path)
    entry = input("Enter full file name: ")
    if os.path.exists(entry):
        size = os.path.getsize(entry)
        if size >  10:
            print(f"Deleting {entry}...")
            time.sleep(1)
            os.remove(entry)
            print(f"{entry} deleted.")
        else:
            print("File is not large enough to delete")
    else:
        print("File not found.")
    
get_size()