from tkinter import *
import tkinter as tk
import time,pygame,datetime
pygame.init()
root=Tk()

root.title("piano")
root.geometry('1352x700+0+0')
root.config(background='#1f5631')

ABC=Frame(root,bg='#1f5629',bd=20,relief=RIDGE)
ABC.grid()

ABC1=Frame(ABC,bg='#1f5629',bd=20,relief=RIDGE)
ABC1.grid()

ABC2=Frame(ABC,bg='#1f5629',relief=RIDGE)
ABC2.grid()

ABC3=Frame(ABC,bg='#1f5629',relief=RIDGE)
ABC3.grid()


str1=StringVar()
str1.set("just like music")
Date1=StringVar()
Time=StringVar()
Date1.set(time.strftime("%d,%m,%y"))
Time.set(time.strftime("%H:%M:%S"))
#lables
l=Label(ABC1,text="just like music",font=("arial",15,"bold"),padx=5,pady=5,fg="black",bd=2,bg='green',justify=CENTER).grid(row=0,column=0,columnspan=11)

txtDisplay=Entry(ABC1,textvariable=str1,font=("arial",10,"bold"),fg="black",bd=10,bg='#ff5467',justify=CENTER).grid(row=1,column=0,pady=1)
txtDate=Entry(ABC1,textvariable=Date1,font=("arial",10,"bold"),fg="black",bd=10,bg='#ff5467',justify=CENTER).grid(row=1,column=1,pady=1)
txtDisplay=Entry(ABC1,textvariable=Time,font=("arial",10,"bold"),fg="black",bd=10,bg='#ff5467',justify=CENTER).grid(row=1,column=2,pady=1)

btncs=Button(ABC2,height=3,width=1,bd=4,text="c#",font=("arial",8,"bold"),fg="white",bg='black',justify=CENTER).grid(row=0,column=0,padx=0,pady=0)

btnD=Button(ABC2,height=3,width=1,bd=4,text="D#",font=("arial",8,"bold"),fg="white",bg='black',justify=CENTER).grid(row=0,column=1,padx=0,pady=0)

btnF=Button(ABC2,height=3,width=1,bd=4,text="F#",font=("arial",8,"bold"),fg="white",bg='black',justify=CENTER).grid(row=0,column=2,padx=5,pady=5)


btnG=Button(ABC2,height=3,width=1,bd=4,text="G#",font=("arial",8,"bold"),fg="white",bg='black',justify=CENTER).grid(row=0,column=3,padx=5,pady=5)

btnBB=Button(ABC2,height=3,width=1,bd=4,text="Bb",font=("arial",8,"bold"),fg="white",bg='black',justify=CENTER).grid(row=0,column=4,padx=0,pady=0)

btnCS1=Button(ABC2,height=3,width=1,bd=4,text="c#1",font=("arial",8,"bold"),fg="white",bg='black',justify=CENTER).grid(row=0,column=5,padx=5,pady=5)


btnDS1=Button(ABC2,height=3,width=1,bd=4,text="D#1",font=("arial",8,"bold"),fg="white",bg='black',justify=CENTER).grid(row=0,column=6,padx=5,pady=5)

root.mainloop()
