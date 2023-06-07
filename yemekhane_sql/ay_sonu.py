import sqlite3
from tkinter import messagebox
import time

a = messagebox.askyesno("Ay sonu","Ay sonu yapıp herkesin kalan hakkını sıfırlamak istediğinize emin misiniz? (Bu işlem geri alınamaz)")


if a:
    b = messagebox.askyesno("Emin misiniz?","Bu işlem geri alınamaz!!")
    if b:
        messagebox.showinfo("10 saniye kaldı!","Sıfırlama işlemi 10 saniye sonra başlayacak!")
        time.sleep(5)
        conn = sqlite3.connect("veri.db")
        c = conn.cursor()
        c.execute("UPDATE ogrenciler SET hak = '0'")
        c.execute("UPDATE ogrenciler SET odedi_mi = '0'")
        conn.commit()
        messagebox.showinfo("Tamamlandı!","Sıfırlama işlemi başarıyla tamamlandı!")
else:
    pass






