import socket
import threading
import sqlite3

# conn = sqlite3.connect("database.db")
# c = conn.cursor()

adamlar = []
dicti = {}

def handle_client(soket, clients):
    print("Handle cli iş başında!")
    while True:
        try:
            message = soket.recv(1024)
            message_decoded = message.decode()
            # mesaj = message_decoded[12:]
            mesaj = message_decoded.split(" ")[2]
            mesaj_liste = message_decoded.split(" ")
            # print("  ",mesaj)
            ad = message_decoded.split(" ")[0]

            if mesaj == "/onlines":
                soket.send(f"SUNUCU ---> {len(clients)-1} kişi aktif!\nAktif olanların listesi:{dicti.values()}".encode())
                
            
                continue            
            if mesaj == "/help":
                soket.send("SUNUCU ---> Komutlar:\n\n/change_password\n/onlines\n\nKomutları yazarak bilgi alabilirsiniz!".encode())
            
            if mesaj[0:5] == "/kick":
                # print("Kick komduuuuu")
                try:
                    atılcak = mesaj_liste[3]     # toSend = f"{nick} ----> {mesaj}".encode()
                except:
                    soket.send("SUNUCU ---> Bu komut '/kick atılcakKişi' şeklinde kullanılır!")
                    continue

                for client in dicti.keys():
                    if dicti[client] == atılcak:
                        client.close()
                        del dicti[client]
                        tosend = f"{atılcak} isimli kişi atıldı!"
                        print(tosend)
                        soket.send("SUNUCU ----> ".decode(),tosend.decode())
                        break
            
            try:
                if mesaj[0:16] == "/change_password":
                    creds = mesaj.split(" ")
                    creds = mesaj.split(" ")
                    if len(creds) == 4:
                        conn = sqlite3.connect("database.db")
                        c = conn.cursor()
                        c.execute("SELECT sifre FROM kullanıcılar WHERE nick = ?",(ad,))
                        gercek_sifre = c.fetchone()[0]
                        conn.close()
                        
                        if creds[1] == gercek_sifre:
                            if creds[2] == creds[3]:
                                yeni_sifre = creds[3]
                                conn = sqlite3.connect("database.db")
                                c = conn.cursor()
                                c.execute("UPDATE kullanıcılar SET sifre = ? WHERE nick = ?",(yeni_sifre,ad))
                                conn.commit()
                                conn.close()
                                soket.send(f"SUNUCU ---> '{gercek_sifre}' olan şifre '{yeni_sifre}' olarak değiştirildi!!".encode())
                                continue
                            else:
                                soket.send("SUNUCU ---> Yeni şifreler aynı değil!".encode())
                                continue
                        else:
                            soket.send("SUNUCU ---> Şu anki şifre yanlış girildi!".encode())
                            continue
                        
                    else:
                        soket.send(f"SUNUCU ---> Bu komut şöyle kullanılır: /change_password 'şuAnkiŞifre' 'yenişifre' 'yenişifre'".encode())
                        continue
            except Exception as E:
                print(E)
            
            print("Mesaj --------------->",message_decoded)
            broadcast(message, soket , clients)
        except:
            soket.close()
            clients.remove(soket)
            break

def broadcast(message, client_socket, clients):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)
                # adamlar.remove(dicti[client_socket])

def sunucu_broadcast(message, clients):
    for client in clients:
        try:
            client.send(message.encode())
        except:
            client.close()
            clients.remove(client)
            # adamlar.remove(dicti[client_socket])

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)
    clients = []

    while True:
        client_socket, addr = server_socket.accept()
        nick = client_socket.recv(1024).decode()
        if nick[0:5] == "/*-+<":
            try:
                isim = nick.split(":")[0][5:]        # client_socket.send(f"/*-+<{nick}:{sifre}".encode())
                print(isim)
                conn = sqlite3.connect("database.db")
                c = conn.cursor()
                c.execute("SELECT sifre FROM kullanıcılar WHERE nick = ?",(isim,))
                gercek_sifre = c.fetchone()[0]
                conn.close()
                gelen_sifre = nick[5:].split(":")[1]
                if gelen_sifre == gercek_sifre:
                    print("Başarılı Giriş!")
                    client_socket.send("Başarılı".encode())
                    sunucu_broadcast(f"SUNUCU ---> {isim} adlı kullanıcı katıldı!",clients)
                    
                    dicti[client_socket] = isim
                
                else:
                    print(f"{nick[0:5]} isimli olmayan kişi :D kişi giriş yapamadı!")
                    client_socket.send("Hatalı Şifre".encode())
                    client_socket.close()
                    continue
                    
            except:
                print("Geçersiz kullanıcı!")
                client_socket.send("Kullanıcı adı bulunamadı!".encode())
                client_socket.close()
                continue

        elif nick.split(":")[0] == "++--*/":
            # try:
            isim = nick.split(":")[1]
            print(isim)
            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            c.execute("SELECT COUNT(*) FROM kullanıcılar WHERE nick = ?",(isim,))
            var_mı = c.fetchone()[0]
            conn.close()
            if var_mı == 1:
                client_socket.send("Var".encode())
                client_socket.close()
                continue
            if var_mı == 0:
                conn = sqlite3.connect("database.db")
                c = conn.cursor()
                c.execute("INSERT INTO kullanıcılar VALUES (?,?)",(nick.split(":")[1],nick.split(":")[2]))
                conn.commit()
                conn.close()
                print("Kullanıcı kaydoldu!")
                client_socket.send("Kayıt Başarılı".encode())
                client_socket.close()
                continue
        else:
            print("Geçersiz talep!")
            client_socket.close()
            continue

        clients.append(client_socket)
        print(f"Bağlandı: {addr}, Kullanıcı Adı: {nick[5:]}")
        thread = threading.Thread(target=handle_client, args=(client_socket, clients))
        thread.start()

start_server()