import os
import time

def run_program():
    path = "C:\\Users\\azizurrohman\\Desktop\\py" # location of program
    os.chdir(path)
    entry = input("Run program Y or N ")
    if entry.lower() == "y":
        print("Running program...")
        time.sleep(1)
        exec(open("hello-world.py").read()) # choose the program you want to run
    else:
        print("Quitting program")
        quit()
        
run_program()