import serial.tools.list_ports
import json
import os
from playsound import playsound
from tkinter import *

window = Tk()
window.geometry("700x500")

ports=serial.tools.list_ports.comports()

serialInst = serial.Serial()

portlist=[]

for oneport in ports:
    portlist.append(str(oneport))
    print(str(oneport))

val = input("Select port: COM")

for x in range(0,len(portlist)):
    if portlist[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portlist[x])

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()


window.mainloop()


while True:
    while True:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            cardn = packet.decode("utf").rstrip("\n")
            cardr = cardn.rstrip("\r")
            card = cardr.rstrip(" ")
            print(card)
            if card == "4 32 49 115":
                print("Özel Geçiş! Hoş Geldiniz!\n")
                playsound(r"C:\Users\Deniz\Documents\Python\yemekhanev2\vip.mp3")
                break
            try:
                file = r"C:\Users\Deniz\Documents\Python\yemekhanev2\veri\uid\-" + card + ".json"
                with open(file) as f:
                    veri = json.load(f)
                print("Veri alındı!")
            except:
                print("Geçersiz Kart! / HATA")
                playsound(r"C:\Users\Deniz\Documents\Python\yemekhanev2\invaild.mp3")
                break
            if int(veri["Kalan"]) > 0:
                os.remove(file)
                yenikalan = int(veri["Kalan"]) - 1
                kisi_dicteksi = {"isim":veri["isim"],"Soy isim":veri["Soy isim"],"Numara":veri["Numara"],"Kalan":yenikalan,"ID":veri["ID"]}
                with open(file, 'w') as json_dosya:
                    json.dump(kisi_dicteksi, json_dosya,ensure_ascii=False)
                print("İsim: ",veri["isim"])
                print("Soy isim: ",veri["Soy isim"])
                print("Kalan: ",yenikalan)
                print("UUID: ",veri["ID"])
                print("Okul Numarası",veri["Numara"])
                print("GEÇİŞ BAŞARILI!!\n")
                playsound(r"C:\Users\Deniz\Documents\Python\yemekhanev2\basarili.mp3")
            else:
                print("İsim: ",veri["isim"])
                print("Soy isim: ",veri["Soy isim"])
                print("Kalan: ",veri["Kalan"])
                print("UUID: ",veri["ID"])
                print("Okul Numarası",veri["Numara"])
                print("Geçiş BAŞARISIZ!!\n")
                playsound(r"C:\Users\Deniz\Documents\Python\yemekhanev2\yetersiz.mp3")