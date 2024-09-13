from tkinter import *
import random

root=Tk()
root.title("Dice Roll")
root.geometry("700x450")

label = Label(root, text="", font=("times", 260))

def roll():
    # These all indicate the 1,2,3,4,5,6 dots on dice, first indicates 1 dot, second indicates 2 dots etc.
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
    label.pack()

button = Button(root, text="Let us roll!", width=40, height=5, font=10, bg="white", bd=2, command=roll)
button.pack(padx=10, pady=10)

root.mainloop()