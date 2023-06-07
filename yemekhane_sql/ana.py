import serial.tools.list_ports
import json
import os
from playsound import playsound
from tkinter import *
import threading
from PIL import Image,ImageTk
import time
import pickle
from tkinter import messagebox
import sqlite3

bos = []
card_list = []
numlist = []
son = 0

window = Tk()
window.geometry("650x450")
window.title("HFL Yemekhane")

try:
    with open("num.pkl","rb") as f:
        numlist = pickle.load(f)
    with open("card.pkl","rb") as f:
        card_list = pickle.load(f)
    gun_sonu = messagebox.askyesno("Gün Başı Algılandı!", "Gün sonu yapmak ister misiniz?")
    if gun_sonu:
        with open("num.pkl","rb") as f:
            numlist = pickle.load(f)
        with open("card.pkl","rb") as f:
            card_list = pickle.load(f)
        if len(numlist) != len(card_list):
            messagebox.showerror("Kritik Olmayan Hata!",f"Liste Uzunlukları Aynı Değil!\n cardlist:{len(card_list)}\nnumlist:{len(numlist)}")
        else:
            pass
        gun_sonu_2 = messagebox.askyesno("Emin misiniz?", "Gün sonu yapmak istediğinizden emin misiniz?\nBu işlem geri alınamaz!")
        if gun_sonu_2:
            messagebox.showinfo("Bilgi",f"Bugün {len(card_list)} kişi yemek aldı!")

            os.remove("num.pkl")
            os.remove("card.pkl")
            son = 1
        else:
            messagebox.showinfo("Bilgi",f"Bugün {len(card_list)} kişi yemek aldı!")
            son = 1
    else:
        messagebox.showinfo("Aynı Gün","Aynı günden devam ediliyor!")

except:
    isteme = messagebox.askyesno("Gün Başı", "Gün başı yapmak ister misiniz?")
    if isteme:
        with open("num.pkl","wb") as f:
            pickle.dump(bos,f)
        with open("card.pkl","wb") as f:
            pickle.dump(bos,f)
    else:
        messagebox.showinfo("Program Kapandı","Gün Başı olmadan program kullanılamaz!!")
        exit()

if son:
    exit()
else:
    pass

def close():
    with open("num.pkl","wb") as f:
        pickle.dump(numlist,f)
    with open("card.pkl","wb") as f:           #Uygulama kapatıldığında listeleri .pkl dosyalarına kaydeder ve uygulamayı kapatır.
        pickle.dump(card_list,f)
    window.destroy()
    exit()

window.protocol("WM_DELETE_WINDOW", close)      #Uygulama kapatıldığında close() fonksiyonun çalışması sağlanır.

tik_image = Image.open("tik.png")
tik_image_res = tik_image.resize((90,90), Image.ANTIALIAS)
tik = ImageTk.PhotoImage(tik_image_res)

noiinfo_image = Image.open("nothing.png")
noinfo_image_res = noiinfo_image.resize((90,90), Image.ANTIALIAS)
noinfo = ImageTk.PhotoImage(noinfo_image_res)

cross_image = Image.open("cross.png")
cross_image_res = cross_image.resize((90,90), Image.ANTIALIAS)
cross = ImageTk.PhotoImage(cross_image_res)

credits_image = Image.open("user.ico")
credits_image_res = credits_image.resize((23,23), Image.ANTIALIAS)
credits_ready = ImageTk.PhotoImage(credits_image_res)
credits_lbl = Label(image=credits_ready)

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

def ana():
    while True:
        while True:
            if serialInst.in_waiting:
                packet = serialInst.readline()
                cardn = packet.decode("utf").rstrip("\n")
                cardr = cardn.rstrip("\r")
                card = cardr.rstrip(" ")
                print(card)
                if card in card_list:
                    durum.configure(image=cross)
                    print("Zaten geçen öğrenci")
                    playsound(r"ikinci.mp3")
                    time.sleep(0.2)
                    durum.configure(image=noinfo)
                    break
                if card == "4 32 49 115":
                    print("Özel Geçiş! Hoş Geldiniz!\n")
                    playsound("vip.mp3")
                    break

                try:
                    conn = sqlite3.connect("veri.db")
                    c = conn.cursor()
                    c.execute("SELECT * FROM ogrenciler WHERE id = ?",(card,))
                    liste = c.fetchall()[0]
                    veri = {"isim":liste[0],"Soy isim":liste[1],"Numara":liste[2],"Kalan":liste[3],"Sınıf":liste[4],"ID":liste[5],"Odedi mi":liste[6]}
                    conn.commit()
                    

                except:
                    print("Geçersiz Kart! / HATA")
                    durum.configure(image=cross)
                    playsound("invaild.mp3")
                    time.sleep(0.3)
                    durum.configure(image=noinfo)
                    break

                if int(veri["Kalan"]) > 0:

                    durum.configure(image=tik)
                    if veri["Odedi mi"] == "1":
                        odemetxt = "Ödedi"
                    elif veri["Odedi mi"] == "0":
                        odemetxt = "Ödemedi"
                    else:
                        odemetxt = "HATA"

                    yenikalan = int(veri["Kalan"]) - 1
                    c.execute("UPDATE ogrenciler SET hak = ? WHERE id = ?",(yenikalan,card))
                    conn.commit()
                    numlist.append(veri["Numara"])
                    card_list.append(card)

                    print("İsim: ",veri["isim"])
                    print("Soy isim: ",veri["Soy isim"])
                    print("Kalan: ",veri["Kalan"])
                    print("UUID: ",veri["ID"])
                    print("Okul Numarası",veri["Numara"])
                    print("GEÇİŞ BAŞARILI!!\n")

                    isimlabel.configure(text="İsim: " + veri["isim"])
                    soyisimlabel.configure(text="Soy İsim: " + veri["Soy isim"])
                    haklabel.configure(text="Kalan Hak: " + str(yenikalan))
                    idlabel.configure(text="ID: " + veri["ID"])
                    numaralabel.configure(text="Okul Numarası: " + str(veri["Numara"]))
                    odemelabel.configure(text="Ödedi mi? :" + odemetxt)
                    sinif_label.configure(text="Sınıf: "+veri["Sınıf"])

                    playsound("basarili.mp3")
                    if odemetxt == "Ödemedi":
                        playsound("odenmedi.mp3")
                    time.sleep(0.3)
                    durum.configure(image=noinfo)
                    conn.commit()
                    conn.close()
                else:
                    durum.configure(image=cross)
                    isimlabel.configure(text="İsim: " + veri["isim"])
                    soyisimlabel.configure(text="Soy İsim: " + veri["Soy isim"])
                    haklabel.configure(text="Kalan Hak: " + str(veri["Kalan"]))
                    idlabel.configure(text="ID: " + veri["ID"])
                    numaralabel.configure(text="Okul Numarası: " + veri["Numara"])
                    sinif_label.configure(text="Sınıf: "+veri["Sınıf"])

                    print("İsim: ",veri["isim"])
                    print("Soy isim: ",veri["Soy isim"])
                    print("Kalan: ",veri["Kalan"])
                    print("UUID: ",veri["ID"])
                    print("Okul Numarası",veri["Numara"])
                    print("Geçiş BAŞARISIZ!!\n")
                    playsound(r"yetersiz.mp3")
                    time.sleep(0.3)
                    durum.configure(image=noinfo)

def no_gecis():
    while True:
        global card_list
        numaraa = no_entry.get()

        if numaraa in numlist:
            durum.configure(image=cross)
            print("Zaten geçen öğrenci")
            playsound(r"ikinci.mp3")
            time.sleep(0.2)
            durum.configure(image=noinfo)
            break

        try:
            conn = sqlite3.connect("veri.db")
            c = conn.cursor()
            c.execute("SELECT * FROM ogrenciler WHERE numara = ?",(numaraa,))
            liste = c.fetchall()[0]
            veri = {"isim":liste[0],"Soy isim":liste[1],"Numara":liste[2],"Kalan":liste[3],"Sınıf":liste[4],"ID":liste[5],"Odedi mi":liste[6]}
            conn.commit()
            
        
        except:
            print("Geçersiz Numara! / HATA")
            durum.configure(image=cross)
            playsound("invaild.mp3")
            time.sleep(0.3)
            durum.configure(image=noinfo)
            break

        if int(veri["Kalan"]) > 0:
            durum.configure(image=tik)
            yenikalan = int(veri["Kalan"]) - 1
            c.execute("UPDATE ogrenciler SET hak = ? WHERE numara = ?",(yenikalan,numaraa))
            conn.commit()
            conn.close()
            numlist.append(numaraa)
            card_list.append(veri["ID"])

            if veri["Odedi mi"] == 1:
                odemetxt = "Ödedi"
            elif veri["Odedi mi"] == 0:
                odemetxt = "Ödemedi"
            else:
                odemetxt = "HATA!!!"
            print("İsim: ",veri["isim"])
            print("Soy isim: ",veri["Soy isim"])
            print("Kalan: ",yenikalan)
            print("UUID: ",veri["ID"])
            print("Okul Numarası",veri["Numara"])
            print("GEÇİŞ BAŞARILI!!\n")

            isimlabel.configure(text="İsim: " + veri["isim"])
            soyisimlabel.configure(text="Soy İsim: " + veri["Soy isim"])
            haklabel.configure(text="Kalan Hak: " + str(yenikalan))
            idlabel.configure(text="ID: " + veri["ID"])
            numaralabel.configure(text="Okul Numarası: " + str(veri["Numara"]))
            odemelabel.configure(text="Ödedi mi? :" + odemetxt)
            sinif_label.configure(text="Sınıf: "+veri["Sınıf"])

            playsound("basarili.mp3")
            if odemetxt == "Ödemedi":
                playsound("odenmedi.mp3")
            time.sleep(0.3)
            durum.configure(image=noinfo)
            break
        else:
            durum.configure(image=cross)
            isimlabel.configure(text="İsim: " + veri["isim"])
            soyisimlabel.configure(text="Soy İsim: " + veri["Soy isim"])
            haklabel.configure(text="Kalan Hak: " + str(veri["Kalan"]))
            idlabel.configure(text="ID: " + veri["ID"])
            numaralabel.configure(text="Okul Numarası: " + veri["Numara"])
            sinif_label.configure(text="Sınıf: "+veri["Sınıf"])

            print("İsim: ",veri["isim"])
            print("Soy isim: ",veri["Soy isim"])
            print("Kalan: ",veri["Kalan"])
            print("UUID: ",veri["ID"])
            print("Okul Numarası",veri["Numara"])
            print("Geçiş BAŞARISIZ!!\n")
            playsound(r"yetersiz.mp3")
            time.sleep(0.3)
            durum.configure(image=noinfo)
            break

def gecis_thread():
    threading.Thread(target=no_gecis).start()

def credits():
    yapan = "Arayüz Tasarımı: Deniz Eren Yıldırım\n\nVeri Tabanı Yazılımları: Deniz Eren Yıldırım\n\nAna Yazılım: Deniz Eren Yıldırım\n\nArduino Haberleşmesi: Deniz Eren Yıldırım"
    messagebox.showinfo("Emeği Geçenler", yapan)

def nolur_nolmaz():
    while True:
        time.sleep(30)
        with open("num.pkl","wb") as f:                       #Bu fonksiyon başka bir threadde sürekli olarak 30 sn de
            pickle.dump(numlist,f)                            #bir çalışarak uygulamanın çökme ihtimalinin sonucu olan
        with open("card.pkl","wb") as f:                      #o gün geçenlerin kaydolmaması ihtitimalini ortadan kaldırır.
            pickle.dump(card_list,f)


title = Label(window,text="Ana Program",font=("Arial",24))
isimlabel = Label(window,text="İsim:",font=("Arial",20))
soyisimlabel = Label(window,text="Soy İsim:",font=("Arial",20))
haklabel = Label(window,text="Kalan Hak:",font=("Arial",20))
idlabel = Label(window,text="ID:",font=("Arial",20))
numaralabel = Label(window,text="Okul Numarası:",font=("Arial",20))
odemelabel = Label(window,text="Ödedi mi? :",font=("Arial",20))
yapan_lbl = Label(window,text="Yapan: Deniz Eren YILDIRIM",font=8)

sinif_label = Label(window,text="Sınıf: ",font=("Arial",20))

no_entry = Entry(window,width=14,font=("Arial",20))

no_btn = Button(window,text="Öğrenciyi geçir",font=("Arial",16),command=gecis_thread)
credits_btn = Button(window,text="Emeği Geçenler",font=("Arial",9),command=credits)

durum = Label(window,image=noinfo)

tik_canvas = Canvas(window,width=55,height=55)

title.pack()
isimlabel.place(x=5,y=55)
soyisimlabel.place(x=5,y=95)
haklabel.place(x=5,y=135)
idlabel.place(x=5,y=175)
numaralabel.place(x=5,y=213)
odemelabel.place(x=5,y=250)
no_entry.place(x=140,y=350)
no_btn.place(x=360,y=348)
yapan_lbl.place(x=430,y=400)

credits_btn.place(x=5,y=10)
credits_lbl.place(x=105,y=10)

durum.place(x=490,y=90)

sinif_label.place(x=5,y=285)

threading.Thread(target=nolur_nolmaz).start()
threading.Thread(target=ana).start()

window.mainloop()