import socket
import threading
import time
import struct
from tkinter import * 

window = Tk()
window.geometry("400x700")
window.title("HİHİHİAHAH")
window.resizable(False,False)

clients = []

host = '127.0.0.1' 
port = 15426  
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print("[*] Sunucu %s:%d adresinde dinlemede" % (host, port))

def broadcast(messagess):
    message = pad_string_with_spaces(messagess, 50).encode()
    for client in clients:
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

def accept():
    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        print("[*] %s:%d adresinden bağlandı" % (addr[0], addr[1]))

def hahaha():
    broadcast("haha")

def kask():
    broadcast("kask")

def kemal():
    broadcast("kemal")

def recep():
    broadcast("recep")

def okaner():
    broadcast("okaner")

haha_btn = Button(window,bg="#c8cbcf",text="Hihihahah!",font=("Arial",20),command=hahaha,width=400).pack(pady=10)

kask_btn = Button(window,bg="#f75757",text="Kaskımı Geri Ver!",font=("Arial",20),command=kask,width=400).pack(pady=10)

kemal_btn = Button(window,bg="#f067a7",text="Sana Söz!",font=("Arial",20),width=400,command=kemal).pack(pady=10)

recep_btn = Button(window,bg="#f58e20",text="Böhöhöhöyt!",font=("Arial",20),width=400,command=recep).pack(pady=10)

okaner_btn = Button(window,bg="#000000",fg="#FFFFFF",text="Okaner!",font=("Arial",20),width=400,command=okaner).pack(pady=10)

client_handler = threading.Thread(target=accept)
client_handler.start()

window.mainloop()