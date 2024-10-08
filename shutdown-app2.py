from tkinter import * 
import os

def restart():
    os.system("shutdown /r /t 1") # it's works as restart command
def restart_time():
    os.system("shutdown /r /t 20") # it's works as restart command with time
def logout():
    os.system("shutdown -l") # it's works as logout command 
def shutdown():
    os.system("shutdown /s /t 1") # it's works as rshoutdown command    

st= Tk()
st.title("Shutdown App") #use to give title to app
st.geometry("500x500")   #use to set geomerty of app
st.config(bg="blue")     #use to set the background color

r_button= Button(st,text="Restart",font=("Time New Roman",20,"bold"),
relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button= Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),
relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button= Button(st,text="Log-out",font=("Time New Roman",20,"bold"),
relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=150,y=270,height=50,width=200)

st_button= Button(st,text="Shutdown",font=("Time New Roman",30,"bold"),
relief=RAISED,cursor="plus",command=shutdown)
st_button.place(x=150,y=370,height=50,width=200)
st.mainloop()