import tkinter as tk
from tkinter import filedialog
import os

def open_word():
    path = "C:\\Users\\azizurrohman\\Desktop"
    os.chdir(path)
    file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
    if file_path:
        os.startfile(file_path)
        
root = tk.Tk()
root.title("File opener")

btn_open_word = tk.Button(root, text="Open word File (.docx)", command=open_word)
btn_open_word.pack(pady=5)

root.mainloop()