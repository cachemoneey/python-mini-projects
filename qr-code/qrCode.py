from tkinter import *
import qrcode

root = Tk()
root.title("QR Code Generator")
root.geometry("1000x550")
root.config(bg="red")
root.resizable(False,False)

# icon image
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

def generate():
    name = title.get()
    text = entry.get()
    qr = qrcode.make(text)
    qr.save("Qrcode/" + str(name) + ".png") 
    
    global Image
    Image = PhotoImage(file="Qrcode/" + str(name) + ".png")
    Image_view.config(image=Image)

Image_view = Label(root, bg="red")
Image_view.pack(padx=50, pady=10, side=RIGHT)

Label(root, text="Title", fg="white", bg="red", font=15).place(x=50, y=170)

title=Entry(root, width=13, font="Arial 15")
title.place(x=50, y=200)

entry=Entry(root, width=28, font="Arial 15")
entry.place(x=50, y=250)

Button(root, text="Generate", width=20, height=2, bg="grey", fg="black", command=generate).place(x=50, y=300)

root.mainloop()