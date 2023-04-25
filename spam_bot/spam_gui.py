import cmath
import re
from tracemalloc import start
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
import time
import random
from tkinter import *
from PIL import Image,ImageTk
import webbrowser
from tkinter import messagebox
import threading

messagelist = []
logo = Image.open(r"C:\Users\Deniz\Documents\Python\bot\spam.png")
window = Tk()
window.title("Spamcı Bot")
window.geometry("450x530")
window.iconbitmap(r"C:\Users\Deniz\Documents\Python\bot\158610.ico")
editt = r"C:\Users\Deniz\Documents\Python\bot\edit.ico"
edit_ico = Image.open(editt)
start_path = r"C:\Users\Deniz\Documents\Python\bot\start.ico"
start_ico = Image.open(start_path)
save_path = r"C:\Users\Deniz\Documents\Python\bot\save.ico"
save_ico = Image.open(save_path)
help_path = r"C:\Users\Deniz\Documents\Python\bot\help.ico"
help_ico = Image.open(help_path)


def spamla():
    global driver
    state.configure(text = "Durum:QR kodu okutunuz!!\n   Okuttuyssanız Başla'ya Basınız!!")
    driver = webdriver.Chrome(executable_path = r'C:\Users\Deniz\Documents\Python\selenium\chromedriver.exe')
    driver.implicitly_wait(3)
    driver.get("https://web.whatsapp.com/")
    basla.place(x=130,y=390)
    start_canvas.place(x=75,y=385)
    
def ac():
    webbrowser.open(r"C:\Users\Deniz\Documents\Python\bot\kelimeler.txt")

def save():
    with open (r"C:\Users\Deniz\Documents\Python\bot\kelimeler.txt",'r', encoding = 'utf-8') as messages:
        global messagelist
        messagelist = list()
        text = messages.read()
        messagelist = text.split('\n')
        inform = f"Kelimeleriniz: {messagelist}"
    messagebox.showinfo("Kelimeleriniz Kaydedildi", inform)

def basla():
    sayı = 0
    global window
    state.configure(text = "Durum:Spam Başladı!!")
    time.sleep(2)
    message_area = driver.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    message_area.click()
    state.configure(text = "Durum:Spam Başladı!!")
    time.sleep(2)
    while True:
        msgToSend = ".."
        msgToSend = random.choice(messagelist)
        if msgToSend == "" or msgToSend == " ":
            msgToSend = random.choice(messagelist)
        else:
            pass
        # time.sleep(0.05)
        message_area.send_keys(msgToSend)
        # time.sleep(0.05)
        send_btn = driver.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
        # time.sleep(0.05)
        send_btn.click()
        sayı += 1
        print(sayı)

def inf():
    messagebox.showinfo("Yardım","1.Adım-->Başla!! Butonunda tıklayın.\n2.Adım-->Açılan penceredeki QR kodu telefonunuzdan okutunuz.\n3.Adım-->QR kodu okuttuktan sonra spamlamak istediğiniz kişiyle olan sohbetinizi açınız.\n4.Adım-->Kelimeleri düzenlemek için 'Kelimeleri Düzenle'ye tıklayın ve kelimeleri değiştirin.\n5.Adım-->Kelimeleri düzenledikten sonra 'Kelimeleri Kaydet'e tıklamayı unutmayınız.\n6.Adım-->'Spama Başla'ya tıklayın. Spam birkaç saniye içinde başlayacaktır. Spamı durdurmak için tarayıcıyı kapatabilirsiniz.")

resized_logo = logo.resize((419,67), Image.ANTIALIAS)
logo_2 = ImageTk.PhotoImage(resized_logo)
save_ico_res = save_ico.resize((40,40), Image.ANTIALIAS)
save_ico_res_fin = ImageTk.PhotoImage(save_ico_res)
help_ico_res = help_ico.resize((24,24), Image.ANTIALIAS)
help_ico_res_fin = ImageTk.PhotoImage(help_ico_res)


resized_start = start_ico.resize((40,40), Image.ANTIALIAS)
save_canvas = Canvas(window,width=55,height=55)
start_canvas = Canvas(window,width=55,height=55)
edit_canvas = Canvas(window,width=70,height=70)
canvas = Canvas(window,width=429,height=77)
help_canvas = Canvas(window,width=50,height=50)
canvas.pack()
resized_edited = edit_ico.resize((30,30), Image.ANTIALIAS)
resized_edited_i = ImageTk.PhotoImage(resized_edited)
res = ImageTk.PhotoImage(resized_start)

spamla = Button(window,text = "Başla!!",width= 12,height=1,command=spamla,font=("Agency FB",17))
credit = Label(window,text="Made by deno832",font=("Agency FB",17))
info = Label(window,text="Spamlanacak kelimeleri kelimeler.txt'nin içine yazınız!!",font=("Agency FB",18))
words = Label(window,text=messagelist,font=("Agency FB",15))
state = Label(window,text="Durum:Çalışmıyor!!",font =("Arial",18))
basla = Button(window,text="Spama Başla!!",width= 12,height=1,font =("Arial",17),command=basla)
ac_btn = Button(window,text = "Kelimeleri \n Düzenle",command=ac)
save = Button(window,text="Kelimeleri\n Kaydet",command=save)
info_msg = Button(window,text="Yardım",command=inf)

spamla.place(x=158,y=140)
credit.place(x=320,y=80)
info.place(x=15,y=195)
words.place(x=15,y=250)
state.place(x=10,y=290)
canvas.create_image(10,10,anchor = NW , image=logo_2)
start_canvas.create_image(10,10,anchor = NW , image=res)
edit_canvas.create_image(10,10,anchor = NW , image=resized_edited_i)
save_canvas.create_image(10,10,anchor = NW , image=save_ico_res_fin)
help_canvas.create_image(10,10,anchor=NW,image=help_ico_res_fin)
edit_canvas.place(x=245,y=235)
save.place(x=25,y=240)
ac_btn.place(x=185,y=240)
save_canvas.place(x=77,y=231)
info_msg.place(x=360,y=247)
help_canvas.place(x=401,y=238)

window.mainloop()