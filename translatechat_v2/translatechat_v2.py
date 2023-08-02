from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
from tkinter import *
import threading
from deep_translator import GoogleTranslator

eng_translater = GoogleTranslator(source='tr', target='en')
tr_translator = GoogleTranslator(source='en', target='tr')
sent_msgs = []

window = Tk()
window.title("Translate Chat")
window.geometry("500x750")
window.resizable(width=False, height=False)

driver = webdriver.Chrome()
driver.implicitly_wait(3)              # WHATSAPP WEB SİTESİNİ AÇ
driver.get("https://web.whatsapp.com/") 


def gonder():              # GÖNDER BUTONUNA BASILDIĞINDA TETİKLENECEK OLAN FONKSİYON
    global msg_entry
    global driver
    msg_get = msg_entry.get()
    msg_entry.delete(0, END)
    out = eng_translater.translate(msg_get)
    sent_msgs.append(out)
    out_text = out
    msg = f"Sen--> {msg_get}"
    msg_box.insert(END,"\n"+msg)
    message_area = driver.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    message_area.click()
    message_area.send_keys(out_text)
    send_btn = driver.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    send_btn.click()
    msg_entry.delete(0, END)


def cevir_thread():
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    ilk_uzunluk = len(soup.find_all(class_="_11JPr selectable-text copyable-text"))

    while True:
        time.sleep(0.1)     # PC ÇÖKMESİN DİYE BEKLEME

        source = driver.page_source
        soup = BeautifulSoup(source, 'html.parser')          # SÜREKLİ MESAJLARI ALMA
        mesajlar = soup.find_all(class_="_11JPr selectable-text copyable-text")
        
        if len(mesajlar) > ilk_uzunluk:    # YENİ MESAJIN GELİP GELMEDİĞİNE BAKMA
            if mesajlar[len(mesajlar)-1].text in sent_msgs:     # MESAJI BİZİM ATIP ATMADIĞIMIZA BAKMA
                continue
            cevrilmis_txt = tr_translator.translate(mesajlar[len(mesajlar)-1].text)   # MESAJI ÇEVİRİP DEĞİŞKENE ATAMA
            goruncek = f"O ---> {cevrilmis_txt}"
            msg_box.insert(END,"\n"+goruncek)      # SOHBET KUTUSUNA GELEN MESAJI YERLEŞTİRME
            ilk_uzunluk = len(mesajlar)

def on_enter_press(event):
    gonder()

def basla():
    info.destroy()          # ESKİ ELEMENTLERİ SİL
    basla_btn.destroy()

    msg_entry.pack(side=LEFT, anchor=SW,pady=13,padx=4)
    send_btn.pack(side=RIGHT, anchor=SW, pady=7,padx=5)       # YENİLERİNİ EKLE
    msg_box.place(x=10,y=50)
    
    threading.Thread(target=cevir_thread).start()
    window.bind("<Return>", on_enter_press)

Label(window,text="TranslateChat Şeysi",font=("Arial",24)).pack()               # Başlık Yazısı
info = Label(window, text="QR Kodu Okutup Başlaya Tıklayın!",font=("Arial",20))
basla_btn = Button(window,text="Başla",font=("Arial",25), command=basla)         # Başlama Buton 

msg_entry = Entry(window,width=30,font=("Arial",17))
send_btn = Button(window,text="Gönder",font=("Arial",15),command=gonder)         # ÇALIŞMA ESNASINDAKİ ELEMENTLER
msg_box = Text(window,height=28,width=43,font=("Arial",15))

info.pack(pady=200)
basla_btn.place(x=200,y=400)


window.mainloop()