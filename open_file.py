import tkinter as tk
from tkinter import filedialog

def open_dialogue_box():
    filename = filedialog.askopenfilename()
    print("File: ", filename)
    
root = tk.Tk()
root.withdraw()

open_dialogue_box()