import json
from tkinter import * 
import threading
import serial.tools.list_ports
import keyboard
import time
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import sqlite3

conn = sqlite3.connect("veri.db")

c = conn.cursor()

num_dosyalar = []
uid_dosyalar = []

window = Tk()
window.geometry("600x400")
window.title("Veri Tabanı Kayıt")
window.iconbitmap("up-arrow.ico") 

save_image = Image.open("save.ico")
save_image_res = save_image.resize((35,35), Image.ANTIALIAS)
save = ImageTk.PhotoImage(save_image_res)
save_label = Label(window,image=save)

cek_image = Image.open("cek.ico")
cek_image_res = cek_image.resize((30,30), Image.ANTIALIAS)
cek = ImageTk.PhotoImage(cek_image_res)
cek_label = Label(window,image=cek)

odeme = IntVar()
sinif_value = StringVar()

ports=serial.tools.list_ports.comports()
serialInst = serial.Serial()

portlist=[]

for oneport in ports:
  portlist.append(str(oneport))
  print(str(oneport))
  
val = input("Select port: COM")

for x in range(0,len(portlist)):
  if portlist[x].startswith("COM" + str(val)):
    portVar = "COM" + str(val)
    print(portlist[x])

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

def uid_paste():
  while True:
    if serialInst.in_waiting:
      packet = serialInst.readline()
      cardn = packet.decode("utf").rstrip("\n")
      cardr = cardn.rstrip("\r")
      card = cardr.rstrip(" ")
      identry.delete(0, END)
      identry.insert(END,card)

# def pull_func():
#   num = r"C:\Users\okul131\Documents\python project\v8\veri\numara\-" + numaraentry.get() + ".json"
#   with open(num) as f:
#     veri = json.load(f)
#   isimentry.insert(END,veri["isim"])
#   soyisimentry.insert(END,veri["Soy isim"])
#   hakentry.insert(END,veri["Kalan"])
#   identry.insert(END,veri["ID"])
#   odeme.set(veri["Odedi mi"])
#   sinif_value.set(veri["Sınıf"])

def kaydet():

  conn = sqlite3.connect("veri.db")
  c = conn.cursor()

  isim = isimentry.get().capitalize()
  soyisim = soyisimentry.get().capitalize()
  hak = hakentry.get()
  uuid = identry.get()
  numara = numaraentry.get()
  odedi_bilgisi = odeme.get()
  sinif = sinif_value.get()

  if uuid == "":
    messagebox.showerror("ID Boş","ID alanı boş bırakılamaz")
    return
  if numara == "":
    messagebox.showerror("Numara Boş","Numara alanı boş bırakılamaz")
    return

  c.execute("SELECT * FROM ogrenciler WHERE numara = ?",(numara,))
  var_mi = c.fetchall()
  print(var_mi)

  if var_mi:
    messagebox.showerror("Kayıtlı","Bu numara zaten kayıtlı")
    return

  c.execute("SELECT * FROM ogrenciler WHERE id = ?",(uuid,))
  var_mi = c.fetchall()

  if var_mi:
    messagebox.showerror("Kayıtlı","Bu kart ID'si zaten kayıtlı")
    return
  
  c.execute("INSERT INTO ogrenciler VALUES (?,?,?,?,?,?,?)",(isim,soyisim,numara,hak,sinif,uuid,odedi_bilgisi))

  isimentry.delete(0, END)
  soyisimentry.delete(0, END)
  hakentry.delete(0, END)
  identry.delete(0, END)
  numaraentry.delete(0, END)
  odeme.set(0)

  conn.commit()
  conn.close()

title = Label(window,text="Veri Tabanı Yazma",font=("Arial",24))
isimlabel = Label(window,text="İsim:",font=("Arial",20))
soyisimlabel = Label(window,text="Soy İsim:",font=("Arial",20))
haklabel = Label(window,text="Kalan Hak:",font=("Arial",20))
idlabel = Label(window,text="ID:",font=("Arial",20))
numaralabel = Label(window,text="Okul Numarası:",font=("Arial",20))

isimentry = Entry(window,width=25,font=("Arial",15))
soyisimentry = Entry(window,width=25,font=("Arial",15))
hakentry = Entry(window,width=25,font=("Arial",15))
identry = Entry(window,width=25,font=("Arial",15))
numaraentry = Entry(window,width=7,font=("Arial",15))

kayıt = Button(window,text="Kaydet",font=("Arial",18),command=kaydet)
# pull = Button(window,text="Numaradan\nBilgi Çek",command=pull_func)

odedi = Checkbutton(window, text='Ödedi',font=("Arial",16),variable=odeme, onvalue=1, offvalue=0)

sinif_spin = Spinbox(window,font=("Arial",16),width=5,textvariable=sinif_value,values=("9A","9B","9C","9D","9E","10A","10B","10C","10E","11A","11B","11C","11D","11E","12A","12B","12C","12D","12E"))
sinif_lbl = Label(window,text="Sınıf:",font=("Arial",20))

title.pack()
isimlabel.place(x=5,y=55)
soyisimlabel.place(x=5,y=95)   
haklabel.place(x=5,y=135)      #Yazılar
idlabel.place(x=5,y=175)
numaralabel.place(x=5,y=210)

isimentry.place(x=70,y=63)
soyisimentry.place(x=128,y=101)
hakentry.place(x=145,y=142)       #Entry widgetlar
identry.place(x=50,y=180)
numaraentry.place(x=200,y=217)

kayıt.place(x=225,y=315)
# pull.place(x=310,y=212)       #Butonlar

save_label.place(x=320,y=320)
# cek_label.place(x=388,y=214)

odedi.place(y=130,x=450)

sinif_lbl.place(x=5,y=255)
sinif_spin.place(x=85,y=260)

def enterlama():
  while True:
    time.sleep(0.001)
    if keyboard.is_pressed("enter") == True:
      kaydet()
      time.sleep(1)
    else:
      time.sleep(0.001)

threading.Thread(target=enterlama).start()
threading.Thread(target=uid_paste).start()

window.mainloop()