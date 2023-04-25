import sqlite3

conn = sqlite3.connect("veri.db")
c= conn.cursor()

c.execute("INSERT INTO users VALUES ('Deniz','123456')")

conn.commit()