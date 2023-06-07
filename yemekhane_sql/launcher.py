from tkinter import * 
import os
import webbrowser

window = Tk()
window.geometry("600x200")
window.title("Başlatıcı")

def kayit_ac():
    webbrowser.open(r"C:\Users\Deniz\Documents\Python\yemekhanev2\json veri tabanı\veri_tabani_kaydet.py")
def goruntuleme():
    webbrowser.open(r"C:\Users\Deniz\Documents\Python\yemekhanev2\json veri tabanı\veritabanı_çek.py")
def ana():
    webbrowser.open(r"C:\Users\Deniz\Documents\Python\yemekhanev2\deneme.py")

kayit = Button(window,text="Kayıt Ugulaması",font=("Arial",12),command=kayit_ac)
gör = Button(window,text="Görüntüleme Uygulaması",font=("Arial",12),command=goruntuleme)
run = Button(window,text="Çalıştırma Uygulaması",font=("Arial",12),command=ana)

bas = Label(window,text="Başlatıcı",font=("Arial",24))

bas.pack()
kayit.place(x=15,y=90)
gör.place(x=150,y=90)
run.place(x=350,y=90)

window.mainloop()