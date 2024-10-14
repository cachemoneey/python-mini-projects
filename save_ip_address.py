import tkinter as tk
import socket
import time
import os

def start_process():
    ip_address = entry.get()
    try:
        ip = socket.gethostbyname(ip_address)
        print("Please wait...")
        time.sleep(2)
        print("IP:", ip)
        path = "C:\\Users\\azizurrohman\\Desktop"
        os.chdir(path)
        with open("ip_address.txt", "w") as file_object:
            file_object.write(ip)
            print("IP address has been saved to text file")
    except socket.gaierror:
        print("Invalid domain or unable to resolve the IP address.")
        
def clear_process():
    entry.delete(0, tk.END)
    
def quit_program():
    root.destroy()

# create the main window
root = tk.Tk()
root.title("IP Hunter")

# Create a label
label = tk.Label(root, text="Enter A Domain")
label.pack()

# Create a text entry box
entry = tk.Entry(root)
entry.pack()

# Create a button to start the process
button = tk.Button(root, text="Start", command=start_process)
button.pack()

clear_button = tk.Button(root, text="Clear", command=clear_process)
clear_button.pack()

quit_button = tk.Button(root, text="Quit", command=quit_program)
quit_button.pack()

# Run the Tkinter event loop
root.mainloop()