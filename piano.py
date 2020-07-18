from tkinter import *
import tkinter as tk
import time,pygame,datetime
pygame.init()
root=Tk()

def value_cs():
	str1.set('c#')
	sound=pygame.mixer.Sound("Piano/Music_Notes/C_s.wav")
	sound.play()
	
def value_cs1():
	str1.set('c#1')
	sound=pygame.mixer.Sound("Piano/Music_Notes/C_s1.wav")
	sound.play()

def value_ds():
	str1.set('D#')
	sound=pygame.mixer.Sound("Piano/Music_Notes/D_s.wav")
	sound.play()
	
def value_bb():
	str1.set('Bb')
	sound=pygame.mixer.Sound("Piano/Music_Notes/Bb.wav")
	sound.play()

def value_ds1():
	str1.set('D#1')
	sound=pygame.mixer.Sound("Piano/Music_Notes/D_s1.wav")
	sound.play()

def value_g():
	str1.set('G#')
	sound=pygame.mixer.Sound("Piano/Music_Notes/G_s.wav")
	sound.play()
	
def value_f():
	str1.set('F#')
	sound=pygame.mixer.Sound("Piano/Music_Notes/F_s.wav")
	sound.play()
	
	############
	
def value_c():
	str1.set('c')
	sound=pygame.mixer.Sound("Piano/Music_Notes/C.wav")
	sound.play()

def value_d():
	str1.set('D')
	sound=pygame.mixer.Sound("Piano/Music_Notes/D.wav")
	sound.play()
	
def value_e():
	str1.set('E')
	sound=pygame.mixer.Sound("Piano/Music_Notes/E.wav")
	sound.play()

def value_f():
	str1.set('F')
	sound=pygame.mixer.Sound("Piano/Music_Notes/F.wav")
	sound.play()

def value_g():
	str1.set('G')
	sound=pygame.mixer.Sound("Piano/Music_Notes/G.wav")
	sound.play()

def value_a():
	str1.set('A')
	sound=pygame.mixer.Sound("Piano/Music_Notes/A.wav")
	sound.play()
	
def value_b():
	str1.set('B')
	sound=pygame.mixer.Sound("Piano/Music_Notes/B.wav")
	sound.play()
	
def value_e():
	str1.set('E')
	sound=pygame.mixer.Sound("Piano/Music_Notes/E.wav")
	sound.play()	
	
def value_e1():
	str1.set('E1')
	sound=pygame.mixer.Sound("Piano/Music_Notes/E1.wav")
	sound.play()

def value_f1():
	str1.set('F1')
	sound=pygame.mixer.Sound("Piano/Music_Notes/F1.wav")
	sound.play()

def value_d1():
	str1.set('c')
	sound=pygame.mixer.Sound("Piano/Music_Notes/D1.wav")
	sound.play()
	
def value_c1():
	str1.set('c')
	sound=pygame.mixer.Sound("Piano/Music_Notes/C1.wav")
	sound.play()






root.title("piano")
root.geometry('1352x700+0+0')
root.resizable(height = None, width = None)
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
Date1.set(time.strftime("%d-%m-%Y"))
Time.set(time.strftime("%H:%M:%S"))
#lables
l=Label(ABC1,text="MY PIANO",font=("arial",19,"bold"),padx=5,pady=5,fg="#f2ac98",bd=2,bg='#1f5629',justify=CENTER).grid(row=0,column=0,columnspan=11)

txtDisplay=Entry(ABC1,textvariable=str1,font=("arial",8,"bold"),fg="black",bd=8,bg='#ff5467',justify=CENTER).grid(row=1,column=1,pady=1)
txtDate=Entry(ABC1,textvariable=Date1,font=("arial",8,"bold"),fg="black",bd=8,bg='#ff5467',justify=CENTER).grid(row=1,column=0,pady=1)
txttme=Entry(ABC1,textvariable=Time,font=("arial",8,"bold"),fg="black",bd=8,bg='#ff5467',justify=CENTER).grid(row=1,column=2,pady=1)

btncs=Button(ABC2,height=5,width=2,bd=4,text="c#",font=("arial",7,"bold"),command=value_cs,fg="white",bg='black',justify=CENTER).grid(row=0,column=0,padx=3,pady=3)

btnD=Button(ABC2,height=5,width=2,bd=4,text="D#",font=("arial",7,"bold"),fg="white",command=value_ds,bg='black',justify=CENTER).grid(row=0,column=1,padx=3,pady=3)


SPACE1=Button(ABC2,height=5,width=1,state=DISABLED,bg='#1f5629').grid(row=0,column=2)


btnF=Button(ABC2,height=5,bd=4,text="F#",font=("arial",7,"bold"),fg="white",command=value_f,bg='black',justify=CENTER).grid(row=0,column=3,padx=3,pady=3)

btnG=Button(ABC2,height=5,width=2,bd=4,text="G#",font=("arial",7,"bold"),fg="white",command=value_g,bg='black',justify=CENTER).grid(row=0,column=4,padx=3,pady=3)


btNBB=Button(ABC2,height=5,width=2,bd=4,text="Bb",font=("arial",7,"bold"),command=value_bb,fg="white",bg='black',justify=CENTER).grid(row=0,column=5,padx=3,pady=3)



SPACE1=Button(ABC2,height=5,width=1,state=DISABLED,bg='#1f5629').grid(row=0,column=6)


btncs1=Button(ABC2,height=5,width=2,bd=4,text="C#1",font=("arial",7,"bold"),command=value_cs1,fg="white",bg='black',justify=CENTER).grid(row=0,column=7,padx=3,pady=3)


btDS1=Button(ABC2,height=5,width=2,bd=4,text="D#1",font=("arial",7,"bold"),command=value_ds1,fg="white",bg='black',justify=CENTER).grid(row=0,column=8,padx=3,pady=3)

#WHITEKEYS

BTNC=Button(ABC3,height=7,width=2,bd=4,text="C",font=("arial",7,"bold"),command=value_c,bg="white",fg='black').grid(row=0,column=0,padx=3,pady=3)


BTND=Button(ABC3,height=7,width=2,bd=4,text="D",font=("arial",7,"bold"),command=value_d,bg="white",fg='black').grid(row=0,column=1,padx=3,pady=3)


BTNE=Button(ABC3,height=7,width=2,bd=4,text="E",font=("arial",7,"bold"),command=value_e,bg="white",fg='black').grid(row=0,column=2,padx=3,pady=3)


BTNF=Button(ABC3,height=7,width=2,bd=4,text="F",font=("arial",7,"bold"),command=value_f,bg="white",fg='black').grid(row=0,column=3,padx=3,pady=3)


BTNg=Button(ABC3,height=7,width=2,bd=4,text="G",font=("arial",7,"bold"),command=value_g,bg="white",fg='black').grid(row=0,column=4,padx=3,pady=3)


BTNa=Button(ABC3,height=7,width=2,bd=4,text="A",font=("arial",7,"bold"),command=value_a,bg="white",fg='black').grid(row=0,column=5,padx=3,pady=3)


BTNC=Button(ABC3,height=7,width=2,bd=4,text="B",font=("arial",7,"bold"),command=value_b,bg="white",fg='black').grid(row=0,column=6,padx=3,pady=3)


BTNC=Button(ABC3,height=7,width=2,bd=4,text="C1",font=("arial",7,"bold"),command=value_c1,bg="white",fg='black').grid(row=0,column=7,padx=3,pady=3)


BTNC=Button(ABC3,height=7,width=2,bd=4,text="D1",font=("arial",7,"bold"),command=value_d1,bg="white",fg='black').grid(row=0,column=8,padx=3,pady=3)


BTNC=Button(ABC3,height=7,width=2,bd=1,text="E1",font=("arial",7,"bold"),command=value_e1,bg="white",fg='black').grid(row=0,column=9,padx=3,pady=3)


BTNC=Button(ABC3,height=7,width=2,bd=1,text="F1",font=("arial",7,"bold"),command=value_f1,bg="white",fg='black').grid(row=0,column=10,padx=3,pady=3)


'''BTNC=Button(ABC3,height=7,width=2,bd=4,text="c",font=("arial",8,"bold"),bg="white",fg='black',justify=CENTER).grid(row=0,column=11,padx=3,pady=3)

'''



root.mainloop()
