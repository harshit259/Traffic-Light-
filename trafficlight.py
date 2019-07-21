import time
from time import sleep
from tkinter import *
import pyttsx3


e = pyttsx3.init('sapi5')
v = e.getProperty('voices')
e.setProperty('voice',v[1].id)
w=Tk()        
w.title("Traffic Light")
w.geometry("600x800")
w.configure(background="grey")
c=Canvas(w, height=650, width=450, bg="white")
c.pack()
r1=c.create_rectangle(180, 70, 310, 470, fill="black")
r2=c.create_rectangle(230, 400, 270, 680, fill="black")
ar1=c.create_arc(180,30,310,110, extent=180, fill="black")

c1=c.create_oval(180,70,310,200, fill="grey") 
c2=c.create_oval(180,200,310,330, fill="grey")
c3=c.create_oval(180,330,310,460, fill="grey")

def red(a):
    c.itemconfig(c1,fill="red") 
    c.itemconfig(c2,fill="grey") 
    c.itemconfig(c3,fill="grey")   
    w.update()
    speak("stop")
    time.sleep(a)
def yellow(a):
    c.itemconfig(c1,fill="grey") 
    c.itemconfig(c2,fill="orange")
    c.itemconfig(c3,fill="grey")  
    w.update()
    speak("wait")
    time.sleep(a)
def green(a):
    c.itemconfig(c1,fill="grey") 
    c.itemconfig(c2,fill="grey") 
    c.itemconfig(c3,fill="green") 
    w.update()
    speak("go")
    time.sleep(a)

def speak(audio):
    e.say(audio)
    e.runAndWait()

while(True):
    red(2)
    yellow(2)
    green(2)
mainloop()
