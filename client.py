import socket 
from threading import Thread 
from tkinter import *
from tkinter import ttk

PORT =8050
IP_ADDRESS = "127.0.0.1"
SERVER = None
BufferSize = 4096

def musicWindow():
    window = Tk()
    window.title("Music Window")
    window.geometry("600x600")
    window.configure(bg="LightSkyBlue")

    selectLabel = Label(window,text="Select Song",bg="LightSkyBlue",font=("Calibri",20))
    selectLabel.place(x=4,y=2)
    listBox = Listbox(window,height=10,width=40,activestyle="dotbox",bg="LightSkyBlue",borderwidth=4,font=("Calibri",20))
    listBox.place(x=20,y=45)
    scrollBar=Scrollbar(listBox)
    scrollBar.place(relheight=1,relx=1)
    scrollBar.config(command=listBox.yview)
    playButton=Button(window,text="Play",width=10,bd=1,bg="SkyBlue",font=("Calibri",10))
    playButton.place(x=30,y=450)
    stop=Button(window,text="Stop",bd=1,width=10,bg="SkyBlue",font=("Calibri",10))
    stop.place(x=200,y=450)
    upload=Button(window,text="Upload",width=10,bd=1,bg="SkyBlue",font=("Calibri",10))
    upload.place(x=30,y=500)
    download=Button(window,text="Download",width=10,bd=1,bg="skyBlue",font=("Calibri",10))
    download.place(x=200,y=500)
    infoLabel=Label(window,text="",fg="blue",font=("Calibri",10))
    infoLabel.place(x=4,y=530)


    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS 

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))
    musicWindow()
setup()