import sqlite3

def get_user_id(nickname):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Kullanıcı adı ve şifreyi kontrol et
    cursor.execute('''
        SELECT id FROM users
        WHERE nickname = ?
    ''', (nickname,))
    user_id = cursor.fetchone()  # Eşleşen kullanıcı varsa ID'sini alır, yoksa None döner
    conn.close()

    if user_id:
        return user_id[0]
    else:
        return user_id[0]
    

def check_if_exists(nickname):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Kullanıcı adı ve şifreyi kontrol et
    cursor.execute('''
        SELECT id FROM users
        WHERE nickname = ?
    ''', (nickname))

    user_id = cursor.fetchone()  # Eşleşen kullanıcı varsa ID'sini alır, yoksa None döner

    conn.close()
    if user_id:
        return True
    else:
        return False
    
def check_credentials(nickname, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Kullanıcı adı ve şifreyi kontrol et
    cursor.execute('''
        SELECT id FROM users
        WHERE nickname = ? AND password = ?
    ''', (nickname, password))

    user_id = cursor.fetchone()  # Eşleşen kullanıcı varsa ID'sini alır, yoksa None döner

    conn.close()

    if user_id:
        return user_id[0]
    else:
        return None

def get_messages_by_id(user1, user2):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM messages WHERE (sender_id = ? AND receiver_id = ?) OR (receiver_id = ? AND sender_id = ?)",(user1,user2,user1,user2))
    conn.commit()
    results = cursor.fetchall()
    conn.close()

    return results