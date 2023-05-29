import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.filedialog as fdialog
import PIL
from PIL import Image,ImageTk
import pyttsx3
import os

root=tk.Tk()
root.title("Text To Speech")
root.geometry('900x550')

#Created a frame
f1=Frame(bg="#305065")
f1.place(width=900,height=550)

label=Label(f1,text="TEXT TO SPEECH COVERTER",bg="sky blue",font=('Times new roman',30),fg="black")
label.place(x=210,y=20)



#Entry Box
e1=Text(f1,font=('Times new roman',15),bg="white")
e1.place(x=60,y=120,width=500,height=400)
#logo
logo=Image.open("C:\\Users\\VENKATESH\\OneDrive\\Pictures\\Saved Pictures\\logo2.webp")
resize_image=logo.resize((50,50))
img=ImageTk.PhotoImage(resize_image)
label=Label(f1,image=img)
label.image=img
label.place(x=120,y=20)

#text
label1=Label(f1,text="Text Here",bg='#305065',font=('Times new roman',13),fg="white")
label1.place(x=60,y=95)


#combo box

label2=Label(f1,text="Select Voice",bg="#305065",font=('Times new roman',13),fg="white")
label2.place(x=650,y=150)


voice=['MALE','FEMALE']
cb1=ttk.Combobox(f1,values=voice)
cb1.place(x=650,y=180)
cb1.set('FEMALE')

label3=Label(f1,text="Select Speed",bg="#305065",font=('Times new roman',13),fg="white")
label3.place(x=650,y=250)

speed=['Slow','Normal','Fast']
cb2=ttk.Combobox(f1,values=speed)
cb2.place(x=650,y=280)
cb2.set('Normal')



#text to speech

def convert():
    v=cb1.get()
    s=cb2.get()
    text_speech=pyttsx3.init()
    answer=e1.get('1.0','end')
    voices=text_speech.getProperty('voices')
    def setvoice():
        if (v=='MALE'):
            text_speech.setProperty('voice',voices[0].id)#male voice
            text_speech.say(answer)
            text_speech.runAndWait()
        else:
            text_speech.setProperty('voice',voices[1].id)#male voice
            text_speech.say(answer)
            text_speech.runAndWait()
    if(answer):
        if(s=='Fast'):
            rate=text_speech.getProperty("rate")
            text_speech.setProperty("rate",250)
            setvoice()
        elif(s=='Normal'):
            rate=text_speech.getProperty("rate")
            text_speech.setProperty("rate",160)
            setvoice()
        else:
            rate=text_speech.getProperty("rate")
            text_speech.setProperty("rate",90)
            setvoice()
    
def save():
    v=cb1.get()
    s=cb2.get()
    text_speech=pyttsx3.init()
    answer=e1.get('1.0','end')
    voices=text_speech.getProperty('voices')
    def setvoice():
        if (v=='MALE'):
            text_speech.setProperty('voice',voices[0].id)#male voice
            text_speech.say(answer)
            path=fdialog.askdirectory()
            os.chdir(path)
            text_speech.save_to_file(answer,"Audio.mp3")
            text_speech.runAndWait()
        else:
            text_speech.setProperty('voice',voices[1].id)#male voice
            text_speech.say(answer)
            path=fdialog.askdirectory()
            os.chdir(path)
            text_speech.save_to_file(answer,"Audio.mp3")
            text_speech.runAndWait()
    if(answer):
        if(s=='Fast'):
            rate=text_speech.getProperty("rate")
            text_speech.setProperty("rate",250)
            setvoice()
        elif(s=='Normal'):
            rate=text_speech.getProperty("rate")
            text_speech.setProperty("rate",160)
            setvoice()
        else:
            rate=text_speech.getProperty("rate")
            text_speech.setProperty("rate",90)
            setvoice()
    

    




#image icon
speak=PhotoImage(file='speak.png')

#covert Button
b1=Button(f1,text="Convert",command=convert,padx=15,pady=10,fg='black',font=('Times new roman',14),bg="light blue")
b1.place(x=670,y=460)

#Download Button
b2=Button(f1,text="Downlaod",command=save,padx=15,pady=10,fg='black',font=('Times new roman',14),bg="light green")
b2.place(x=660,y=360)




root.mainloop()









