import sqlite3
from tkinter import * 
from tkinter import messagebox
import time

def hak_ver():
    try:
        hak_get = hak.get()
        numara_get = numara.get()
        numara.delete(0, END)
        conn = sqlite3.connect("veri.db")
        c = conn.cursor()
        c.execute("UPDATE ogrenciler SET hak = ? WHERE numara = ?",(hak_get,numara_get))
        c.execute("SELECT isim, soy_isim, sinif FROM ogrenciler WHERE numara = ?",(numara_get,))
        liste = c.fetchall()[0]
        conn.commit()
        conn.close()
        messagebox.showinfo("Başarılı!",f"{liste[0]} isimli ,{liste[1]} soy isimli, {liste[2]} sınıfındaki öğrenciye {hak_get} hak verildi!")
    except:
        messagebox.showerror("HATA!","Bir hatayla karşılaşıldı!!")

def odet():
    conn = sqlite3.connect("veri.db")
    c = conn.cursor()
    numara_get = numara.get()
    c.execute("SELECT odedi_mi FROM ogrenciler WHERE numara = ?",(numara_get,))
    odedi_mi = c.fetchall()[0][0]
    print(odedi_mi)
    if odedi_mi == "1":
        messagebox.showerror("HATA!","Bu öğrenci zaten ödemiş!")
        return
    elif odedi_mi == "0":
        pass
    else:
        messagebox.showerror("HATA!","Bu öğrencinin ödeme bilgisi bozuk!(DB Browser ile düzeltiniz!)")
    c.execute("UPDATE ogrenciler SET odedi_mi = '1' WHERE numara = ?",(numara_get,))
    conn.commit()
    conn.close()

window = Tk()
window.geometry("550x370")
window.title("Hak Verme")

title = Label(window,text= "Hak Verme Programı",font=("Arial",20)).pack()

hak = Entry(window,font=("Arial",17),width=4)
hak_lbl = Label(window,text="Hak:",font=("Arial",17))

numara = Entry(window,font=("Arial",23),width=6)
num_lbl = Label(window,text="Numara:",font=("Arial",20))

btn = Button(window,text="Hak Ver",font=("Arial",20),command=hak_ver)
odeme_btn = Button(window,text="Ödedi",font=("Arial",20),command=odet)

hak.place(x=270,y=50)
hak_lbl.place(x=215,y=49)

numara.place(x=275,y=150)
num_lbl.place(x=165,y=150)

btn.place(x=150,y=230)
odeme_btn.place(x=290,y=230)

window.mainloop()