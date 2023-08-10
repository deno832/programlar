import socket
import threading
import time
import struct
import sqlite3
from datetime import datetime
import cv2
import face_recognition
from simple_facerec import SimpleFacerec
import RPi.GPIO as GPIO



clients = []

def handle_client(client_socket):
    while True:
        datas = client_socket.recv(1024)
        # print(clients)

        if not datas:
            break                            
        text = datas.decode()[2:]
        if text == "al":
            
            conn = sqlite3.connect("loglar.db")

            c = conn.cursor()
            c.execute("SELECT * FROM logs")
            
            datas = c.fetchall()
            conn.close()
            for data in datas:
                client_socket.send(pad_string_with_spaces(str(data), 100).encode())
        elif text == "sil":
            conn = sqlite3.connect("loglar.db")

            c = conn.cursor()
            c.execute("DELETE FROM logs")
            
            conn.commit()
            conn.close()
            print("Bütün Veriler Silindi!!")
			
        print(f"Gelen Mesaj: {text}")
        
        
    client_socket.close()
    clients.remove(client_socket)
    print("İstemci Bağlantısı Kesildi!")

def broadcast(messagess, client_socket):
    message = pad_string_with_spaces(messagess, 100).encode()
    for client in clients:
        if client != client_socket:
            client.send(message)
            

def pad_string_with_spaces(input_str, total_bytes):
    # Eğer giriş stringi belirli byte sayısına eşit veya büyükse, input_str'i direkt döndür
    if len(input_str.encode()) >= total_bytes:
        return input_str

    # Gerekli padding miktarını hesapla
    padding_bytes = total_bytes - len(input_str.encode())

    # Boşluk karakteriyle doldur
    padded_str = input_str + ' ' * padding_bytes

    return padded_str


def main():
    host = '192.168.1.214'  # Tüm arayüzlerden gelen bağlantıları dinlemek için
    port = 15425  # Bağlantılar için kullanılacak port numarası

    # IPv4 ve TCP protokolü için bir soket oluştur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Soket ve portu bağla
    server_socket.bind((host, port))

    # Maksimum 5 bağlantıya izin ver
    server_socket.listen(5)

    print("[*] Sunucu %s:%d adresinde dinlemede" % (host, port))
   
    # İstemci bağlantısı kabul et
    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        print("[*] %s:%d adresinden bağlandı" % (addr[0], addr[1]))

        # İstemci ile ilgilenen yeni bir iş parçacığı oluştur
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

def algılama():
    saved_name = ""
	
    print("Başladı!")
    try:
        while True:
            time.sleep(0.01)
            current_state = GPIO.input(pir_sensor)
            while True:
                #print("Hareket Var!!")
                for i in range(100):
                    ret, frame = cap.read()
        
                    face_locations, face_names = sfr.detect_known_faces(frame)

                    for face_loc, name in zip(face_locations, face_names):
                        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                        cv2.putText(frame, name, (x1,y1 -10), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,255), 2)
                        cv2.rectangle(frame,(x1,y1), (x2,y2), (0, 0, 200), 2)
                        if name != saved_name:
                             connection = sqlite3.connect("loglar.db")
                             cursor = connection.cursor()
                             su_an = datetime.now()
                             saat = su_an.strftime("%Y-%m-%d %H:%M:%S")
                             print(saat + " Tarihinde Odaya " + name + " Kişisi Girdi!")
                             cursor.execute(f"INSERT INTO logs VALUES (?,?)", (saat,name))
                             connection.commit()
                             connection.close()
                             #saved_name = name
                print("Hareket Bitti!")
    except KeyboardInterrupt:
        pass
    finally:
        
        GPIO.cleanup()


if __name__ == "__main__":
    conn = sqlite3.connect("loglar.db")
    c = conn.cursor()
    print("Kod Başladı!!")

    sfr = SimpleFacerec()
    sfr.load_encoding_images("./images/")
    cap  = cv2.VideoCapture(0)


    pir_sensor = 11

    GPIO.setmode(GPIO.BOARD)

    

    GPIO.setup(pir_sensor, GPIO.IN)

    current_state = 0
    algı_handler = threading.Thread(target=algılama)
    algı_handler.start()
    main()
