import sqlite3

conn = sqlite3.connect("veri.db")

c = conn.cursor()


c.execute("SELECT isim, soy_isim, sinif FROM ogrenciler WHERE numara = 123")
print(c.fetchall())

conn.close()
