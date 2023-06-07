import os
import json
from tkinter import messagebox
from tkinter import *
import sys
import time
import webbrowser
import sqlite3

conn = sqlite3.connect("odemeyenler.db")
c = conn.cursor()

c.execute("DROP TABLE odemeyenler")
conn.commit()
c.execute("CREATE TABLE odemeyenler(isim text,  soy_isim text,  numara integer,  sınıf text)")

conn.commit()
dosyalar = []

baslangic_zamani = time.time()
dosyalar = []
os.chdir("veri/numara")

odemeyenler = []
alanlar = []

for i in os.listdir(os.getcwd()):
    dosyalar.append(i)
print(dosyalar)

for i in dosyalar:
    with open(i) as f:
        veri = json.load(f)
    if veri["Odedi mi"] == 0 and veri["Kalan"] >= 0:

        overall = [veri["isim"],veri["Soy isim"],veri["Numara"],veri["Sınıf"]]
        c.execute("INSERT INTO odemeyenler VALUES(?,?,?,?)",overall)
        
conn.commit()

for i in dosyalar:
    with open(i) as f:
        veri = json.load(f)
    if veri["Kalan"] >= 0:
        alanlar.append(i)

print(odemeyenler)
print(len(odemeyenler))

def goruntule():
    messagebox.showinfo("Başarılı!s","Ödemeyenlerin yer aldığı veri tabanı dosyası kaydedilmiştir! DB Browser ile açıp çıktı alabilirsiniz.")

window = Tk()
window.title("Veri Tabanı Analiz")
window.geometry("500x300")

baslik = Label(window,text="Veri Tabanı Analiz",font=("Arial",20)).pack()
odemeyenler_lbl = Label(window,font=("Arial",18),text=f"{len(odemeyenler)} Kişi Ödemedi")
kayıtlı_lbl = Label(window,font=("Arial",18),text=f"{len(dosyalar)} Kişi Kayıtlı")
alanlar_lbl = Label(window,font=("Arial",18),text=f"{len(alanlar)} Kişi Bu Ay Kart Aldı")

odemeyenler_btn = Button(window,text="Ödemeyenleri Görüntüle",font=("Arial",14),command=goruntule)

kayıtlı_lbl.place(x=5,y=40)
odemeyenler_lbl.place(x=5,y=75)
alanlar_lbl.place(x=5,y=110)
odemeyenler_btn.place(x=130,y=205)

window.mainloop()