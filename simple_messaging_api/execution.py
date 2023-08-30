import sqlite3

# Veritabanı bağlantısını oluştur
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Kullanıcılar tablosunu oluştur
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY ,
        nickname TEXT NOT NULL,
        password TEXT NOT NULL,
        mail_adress TEXT NOT NULL
    )
''')

# Mesajlar tablosunu oluştur
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        sender_id INTEGER,
        receiver_id INTEGER,
        message_text TEXT NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (sender_id) REFERENCES users (id),
        FOREIGN KEY (receiver_id) REFERENCES users (id)
    )
''')

conn.commit()

conn.close()

print("Veritabanı oluşturuldu.")