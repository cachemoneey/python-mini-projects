# pip install pillow

from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.config(bg="white")
root.resizable(True, True)

def BMI():
    h = float(Height.get())
    w = float(Weight.get())
    
    # convert height into meter
    m = h /100
    bmi = round(float(w/m**2),1)
    label1.config(text=bmi)
    
    if bmi <= 18.5:
        label2.config(text="Underweight!")
        label3.config(text="You have lower weight than normal!")
    
    elif bmi > 18.5 and bmi <= 25:
        label2.config(text="Normal!")
        label3.config(text="You have a healthy weight!")
        
    elif bmi > 25 and bmi <= 30:
        label2.config(text="Overweight!")
        label3.config(text="You have higher weight than normal!")
        
    else:
        label2.config(text="Obese!")
        label3.config(text="Your health may be at risk, if you do not lose weight!")

# icon
icon_image= PhotoImage(file="bmi-calculator/images/icon.png")
root.iconphoto(False, icon_image)

# top
top = PhotoImage(file="bmi-calculator/images/top.png")
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(x=-10, y=-10)

# bottom box
Label(root, width=72, height=18, bg="lightblue").pack(side=BOTTOM)

# two boxes
box = PhotoImage(file="bmi-calculator/images/box.png")
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)

# scale
scale = PhotoImage(file="bmi-calculator/images/scale.png")
Label(root, bg="lightblue").place(x=20, y=310)

######################### Slider 1 ##################################

current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())
    
    size = int(float(get_current_value()))
    img = (Image.open("bmi-calculator/images/man.png"))
    resized_image = img.resize((50, 10+size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550-size)
    secondimage.image = photo2
    
# command to change background color of scale
style = ttk.Style()
style.configure("TScale", background="white")
slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale", command=slider_changed, variable=current_value)
slider.place(x=80, y=250)


#####################################################################


######################### Slider 2 ##################################

current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())
    
# command to change background color of scale
style2 = ttk.Style()
style2.configure("TScale", background="white")
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale", command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)

#####################################################################

# entry box
Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width=5, font="Arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER) # to align text in center
height.place(x=35, y=160)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width=5, font="Arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER) # to align text in center
weight.place(x=255, y=160)
Weight.set(get_current_value2())

# man image
secondimage = Label(root, bg="lightblue")
secondimage.place(x=70, y=530)

Button(root, text="View Report", width=15, height=2, font="Arial 10 bold", bg="#1f6e68", fg="white",command=BMI).place(x=280, y=340)

label1 = Label(root, font="Arial 60 bold", bg="lightblue", fg="#fff")
label1.place(x=125, y=305) 

label2 = Label(root, font="Arial 20 bold", bg="lightblue", fg="#3b3a3a")
label2.place(x=280, y=430) 

label3 = Label(root, font="Arial 10", bg="lightblue", fg="#fff")
label3.place(x=200, y=500) 

root.mainloop()