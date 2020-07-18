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

ABC1=Frame(ABC,bg='#1f5629',bd=20,)
ABC1.grid()

ABC2=Frame(ABC,bg='#1f5629',)
ABC2.grid()

ABC3=Frame(ABC,bg='#1f5629')
ABC3.grid()


str1=StringVar()
str1.set(" Music")
Date1=StringVar()
Time=StringVar()
Date1.set(time.strftime("%d,%m,%y"))
Time.set(time.strftime("%H:%M:%S"))
#lables
l=Label(ABC1,text="MY PIANO",font=("arial",19,"bold"),padx=5,pady=5,fg="#f2ac98",bd=2,bg='#1f5629',justify=CENTER).grid(row=0,column=0,columnspan=11)

txtDisplay=Entry(ABC1,textvariable=str1,font=("arial",8,"bold"),fg="black",bd=8,bg='#ff5467',justify=CENTER).grid(row=1,column=0,pady=1)
txtDate=Entry(ABC1,textvariable=Date1,font=("arial",8,"bold"),fg="black",bd=8,bg='#ff5467',justify=CENTER).grid(row=1,column=1,pady=1)
txttme=Entry(ABC1,textvariable=Time,font=("arial",8,"bold"),fg="black",bd=8,bg='#ff5467',justify=CENTER).grid(row=1,column=2,pady=1)

btncs=Button(ABC2,height=5,width=2,bd=4,text="c#",font=("arial",7,"bold"),fg="white",bg='black',justify=CENTER).grid(row=0,column=0,padx=3,pady=3)

btnD=Button(ABC2,height=5,width=2,bd=4,text="D#",font=("arial",7,"bold"),fg="white",bg='black',justify=CENTER).grid(row=0,column=1,padx=3,pady=3)


SPACE1=Button(ABC2,height=5,width=1,state=DISABLED,bg='#1f5629').grid(row=0,column=2)


btnF=Button(ABC2,height=5,bd=4,text="F#",font=("arial",7,"bold"),fg="white",bg='black',justify=CENTER).grid(row=0,column=3,padx=3,pady=3)

btnG=Button(ABC2,height=5,width=2,bd=4,text="G#",font=("arial",7,"bold"),fg="white",bg='black',justify=CENTER).grid(row=0,column=4,padx=3,pady=3)


btNBB=Button(ABC2,height=5,width=2,bd=4,text="Bb",font=("arial",7,"bold"),fg="white",bg='black',justify=CENTER).grid(row=0,column=5,padx=3,pady=3)



SPACE1=Button(ABC2,height=5,width=1,state=DISABLED,bg='#1f5629').grid(row=0,column=6)


btncs1=Button(ABC2,height=5,width=2,bd=4,text="C#1",font=("arial",7,"bold"),fg="white",bg='black',justify=CENTER).grid(row=0,column=7,padx=3,pady=3)


btDS1=Button(ABC2,height=5,width=2,bd=4,text="D#1",font=("arial",7,"bold"),fg="white",bg='black',justify=CENTER).grid(row=0,column=8,padx=3,pady=3)

#WHITEKEYS

BTNC=Button(ABC3,height=7,width=2,bd=4,text="c",font=("arial",7,"bold"),bg="white",fg='black').grid(row=0,column=0,padx=3,pady=3)


BTNC=Button(ABC3,height=7,width=2,bd=4,text="c",font=("arial",7,"bold"),bg="white",fg='black').grid(row=0,column=1,padx=3,pady=3)


BTNC=Button(ABC3,height=7,width=2,bd=4,text="c",font=("arial",7,"bold"),bg="white",fg='black').grid(row=0,column=2,padx=3,pady=3)


BTNC=Button(ABC3,height=7,width=2,bd=4,text="c",font=("arial",7,"bold"),bg="white",fg='black').grid(row=0,column=3,padx=3,pady=3)


BTNC=Button(ABC3,height=7,width=2,bd=4,text="c",font=("arial",7,"bold"),bg="white",fg='black').grid(row=0,column=4,padx=3,pady=3)


BTNC=Button(ABC3,height=7,width=2,bd=4,text="c",font=("arial",7,"bold"),bg="white",fg='black').grid(row=0,column=5,padx=3,pady=3)


BTNC=Button(ABC3,height=7,width=2,bd=4,text="c",font=("arial",7,"bold"),bg="white",fg='black').grid(row=0,column=6,padx=3,pady=3)


BTNC=Button(ABC3,height=7,width=2,bd=4,text="c",font=("arial",7,"bold"),bg="white",fg='black').grid(row=0,column=7,padx=3,pady=3)


BTNC=Button(ABC3,height=7,width=2,bd=4,text="c",font=("arial",7,"bold"),bg="white",fg='black').grid(row=0,column=8,padx=3,pady=3)


BTNC=Button(ABC3,height=7,width=2,bd=1,text="c",font=("arial",7,"bold"),bg="white",fg='black').grid(row=0,column=9,padx=3,pady=3)


BTNC=Button(ABC3,height=7,width=2,bd=1,text="c",font=("arial",7,"bold"),bg="white",fg='black').grid(row=0,column=10,padx=3,pady=3)


'''BTNC=Button(ABC3,height=7,width=2,bd=4,text="c",font=("arial",8,"bold"),bg="white",fg='black',justify=CENTER).grid(row=0,column=11,padx=3,pady=3)

'''



root.mainloop()
