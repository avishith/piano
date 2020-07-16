from tkinter import *
import time,pygame,datetime
pygame.init()
root=Tk()

root.title("piano")
root.geometry('300x540')
root.config(background='#1f5631')

ABC=Frame(root,bg='#1f5629',bd=20,relief=RIDGE).grid()

ABC1=Frame(ABC,bg='#1f5629',bd=20,relief=RIDGE).grid()
ABC2=Frame(ABC,bg='#1f5629',bd=20,relief=RIDGE).grid()
ABC3=Frame(ABC,bg='#1f5629',bd=20,relief=RIDGE).grid()


str1=StringVar()
str1.set("just like music")
Date1=StringVar()
Time=StringVar()




root.mainloop()
