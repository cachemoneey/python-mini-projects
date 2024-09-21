# pip install pygame

from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.config(bg="#0f1a2b")
root.resizable(False, False)

mixer.init()

def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        ## print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)

def play_song():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-3])
    

# icon 
image_icon = PhotoImage(file=)
root.iconphoto(False, image_icon)

Top = PhotoImage(file=)
Label(root, image=Top, bg="#0f1a2b").pack()

# logo
Logo = PhotoImage(file=)
Label(root, image=Logo, bg="#0f1a2b").place(x=65, y=115)

# buttons
play_button = PhotoImage(file=)
Button(root, image=play_button, bg="#0f1a2b", bd=0, command=play_song).place(x=100, y=400)

stop_button = PhotoImage(file=)
Button(root, image=stop_button, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=30, y=500)

resume_button = PhotoImage(file=)
Button(root, image=resume_button, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=115, y=500)

pause_button = PhotoImage(file=)
Button(root, image=pause_button, bg="#0f1a2b", bd=0, command=mixer.music.pauses).place(x=200, y=500)

# labels
music = Label(root, text="", font=("Arial", 15), fg="white", bg="#0f1a2b")
music.place(x=150, y=340, anchor="center")

# music
Menu = PhotoImage(file=)
Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)

music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=330, y=350, width=560, height=250)

Button(root, text="Open Folder", width=15, height=2, font=("Arial",10,"bold"), fg="white", bg="#21b3de", command=open_folder).place(x=330, y=300)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font=("Arial",10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()