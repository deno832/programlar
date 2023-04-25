from tkinter import *
import time
import keyboard
import os
from PIL import Image,ImageTk
import datetime

alarmM = ""
alarmH = ""
window = Tk()
window.geometry("450x650")
logo = (Image.open("logo.png"))
window.iconbitmap('icon.ico')
window.title("AltF4")

def kapat():
    keyboard.press("alt")
    time.sleep(0.1)
    keyboard.press("f4")
    time.sleep(0.1)
    keyboard.release("alt")
    keyboard.release("f4")
    time.sleep(0.2)


def gizle():
    global alarmM
    global alarmH
    alarmM_int = int(alarmM)
    alarmH_int = int(alarmH)
    window.destroy()
    while(1):
        if(alarmH_int == datetime.datetime.now().hour and alarmM_int == datetime.datetime.now().minute) :
            time.sleep(2)
            kapat()
            kapat()
            kapat()
            kapat()
            kapat()
            kapat()
            kapat()
            kapat()
            kapat()
            kapat()
            kapat()
            time.sleep(1)
            break
        time.sleep(2)
        print("Bekleniyor")


def saat_kaydet():
    global alarmH
    alarmH = saat_entry.get()
    print(alarmH)


def dakika_kaydet():
    global alarmM
    alarmM = dakika_entry.get()
    print(alarmM)


def tamam():
    global alarmM
    global alarmH
    lbl.configure(text="Alarm "+alarmH+":"+alarmM+" 'e kuruldu.")
#    print("Alarm Kurulan saat:"+alarmH)
#    print("Alarm Kurulan dakika:"+alarmM)
#    print("Başlamak İçin Başlata Tıklayınız!!")
resized_logo = logo.resize((419,67), Image.ANTIALIAS)
logo_2 = ImageTk.PhotoImage(resized_logo)


canvas= Canvas(window,width=429,height=77)
canvas.pack()

made_by = Label(window,text="Made by deno832",font=("Agency FB",16))

saat_entry = Entry(window,width=3,font=("Agency FB",40))

dakika_entry = Entry(window,width=3,font=("Agency FB",40))

iki_nokta = Label(window,text=":",font=("Agency FB",70))

saat_kayıt = Button(window,text="Saat\nKayıt",font=("Agency FB",23),width=6,command=saat_kaydet)

dakika_kayıt = Button(window,text="Dakika\nKayıt",font=("Agency FB",23),command=dakika_kaydet)

tamam_btn = Button(window,text="Tamam!",font=("Agency FB",23),command=tamam)

gizle_btn = Button(window,text = "Gizle",font=("Agency FB",23),command=gizle)

lbl = Label(window,text="",font=("Agency FB",25))


made_by.place(x=327,y=77)
saat_entry.place(x=140,y=180)
iki_nokta.place(x=223,y=142)
dakika_entry.place(x=250,y=180)
dakika_kayıt.place(x=250, y=260)
saat_kayıt.place(x=140,y=260)
tamam_btn.place(x=120,y=380)
gizle_btn.place(x=255,y=379)
lbl.place(x=100,y=450)


canvas.create_image(10,10,anchor = NW , image=logo_2)

window.mainloop()