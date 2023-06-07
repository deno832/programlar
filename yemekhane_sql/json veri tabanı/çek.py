from tkinter import *
import json
import threading
import serial.tools.list_ports
import time
import keyboard
from tkinter import messagebox
from PIL import Image,ImageTk
import os

window = Tk()
window.geometry("600x430")
window.title("Veritabanı Görüntüleme")
window.iconbitmap("down-arrow.ico")

search_image = Image.open("search.ico")
search_image_res = search_image.resize((40,40), Image.ANTIALIAS)
search = ImageTk.PhotoImage(search_image_res)
search_label = Label(window,image=search)

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

def bul():
  try:
    try:
      uid = r"veri\uid\-" + identry.get() + ".json"
      with open(uid) as f:
        veri = json.load(f)

      if veri["Odedi mi"] == 1:
        odemetxt = "Ödedi"
      elif veri["Odedi mi"] == 0:
        odemetxt = "Ödemedi"
      
      isimlabel.configure(text="İsim: " + veri["isim"])
      soyisimlabel.configure(text="Soy İsim: " + veri["Soy isim"])
      haklabel.configure(text="Kalan Hak: " + str(veri["Kalan"]))
      idlabel.configure(text="ID: " + veri["ID"])
      numaralabel.configure(text="Okul Numarası: " + veri["Numara"])
      odemelabel.configure(text="Ödeme Bilgisi:" + odemetxt)
      sinif_label.configure(text="Sınıf: "+veri["Sınıf"])

    except:
      num = r"veri\numara\-" + identry.get() + ".json"
      with open(num) as f:
        veri = json.load(f)
      
      if veri["Odedi mi"] == 1:
        odemetxt = "Ödedi"
      elif veri["Odedi mi"] == 0:
        odemetxt = "Ödemedi"

      isimlabel.configure(text="İsim: " + veri["isim"])
      soyisimlabel.configure(text="Soy İsim: " + veri["Soy isim"])
      haklabel.configure(text="Kalan Hak: " + str(veri["Kalan"]))
      idlabel.configure(text="ID: " + veri["ID"])
      numaralabel.configure(text="Okul Numarası: " + veri["Numara"])
      odemelabel.configure(text="Ödeme Bilgisi:" + odemetxt)
      sinif_label.configure(text="Sınıf: "+veri["Sınıf"])
  except:
    messagebox.showerror("Dosya Bulamadı!", "Aranan dosya veri tabanında bulunamadı! Dosya adını kontrol ediniz!")

def gecir():
  pass
  # if int(veri["Kalan"]) > 0:
  #   os.remove(file)
  #   yenikalan = int(veri["Kalan"]) - 1
  #   kisi_dicteksi = {"isim":veri["isim"],"Soy isim":veri["Soy isim"],"Numara":veri["Numara"],"Kalan":yenikalan,"ID":veri["ID"]}
  #   with open(file, 'w') as json_dosya:
  #     json.dump(kisi_dicteksi, json_dosya,ensure_ascii=False)

title = Label(window,text="Veri Tabanı Okuma",font=("Arial",24))
isimlabel = Label(window,text="İsim:",font=("Arial",20))
soyisimlabel = Label(window,text="Soy İsim:",font=("Arial",20))
haklabel = Label(window,text="Kalan Hak:",font=("Arial",20))
idlabel = Label(window,text="ID:",font=("Arial",20))
numaralabel = Label(window,text="Okul Numarası:",font=("Arial",20))
odemelabel = Label(window,text="Ödeme bilgisi:",font=("Arial",20))

sinif_label = Label(window,text="Sınıf:",font=("Arial",20))

identry = Entry(window,width=17,font=("Arial",20))

idbtn = Button(window,text="BUL",font=("Arial",18),command=bul)
gecir_btn = Button(window,text="Öğrenciyi\nGeçir",command=gecir,font=("Arial",14))

title.pack()
isimlabel.place(x=5,y=55)
soyisimlabel.place(x=5,y=95)
haklabel.place(x=5,y=135)
idlabel.place(x=5,y=175)
numaralabel.place(x=5,y=210)
odemelabel.place(x=5,y=247)
sinif_label.place(x=5,y=280)

idbtn.place(x=150,y=338)

identry.place(x=225,y=345)

search_label.place(x=107,y=345)

def enterlama():
  while True:
    time.sleep(0.001)
    if keyboard.is_pressed("enter") == True:
      bul()
      time.sleep(1)
    else:
      time.sleep(0.001)

threading.Thread(target=enterlama).start()
threading.Thread(target=uid_paste).start()

window.mainloop()