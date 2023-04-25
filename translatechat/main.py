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
import keyboard
from googletrans import Translator
import pyautogui
import win32clipboard
import threading

# Kontrol:   X: 849 Y: 942     RGB: (217, 253, 211)

window = Tk()
window.title("TransChat")
window.geometry("800x1200+1100+0")
translater = Translator()


driver = webdriver.Chrome(executable_path = r'C:\Users\Deniz\Documents\Python\selenium\chromedriver.exe')
driver.implicitly_wait(3)
driver.get("https://web.whatsapp.com/")


def yaz(msg):
    global driver
    message_area = driver.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    time.sleep(0.2)
    message_area.send_keys(msg)
    send_btn = driver.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    send_btn.click()

def send():
    global entry
    global driver
    msg_get = entry.get()
    time.sleep(0.01)
    entry.delete(0, END)
    out = translater.translate(msg_get,dest="en",src="tr")
    out_text = out.text
    msg = f"Sen--> {msg_get}"
    msg_box.insert(END,"\n"+msg)
    message_area = driver.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    message_area.click()
    message_area.send_keys(out_text)
    send_btn = driver.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    send_btn.click()
    entry.delete(0, END)

msg_box = Text(window,height=50,width=100,font=("Arial",13))
entry = Entry(window,width=67,font=("Arial",17))
send_btn = Button(window,text="Gönder",font=("Arial",11),command=send)
temizle = Button(window,text="Temizle",font=("Arial",11),command=clean)

msg_box.pack()
entry.place(x=5,y=970)
send_btn.place(x=890,y=970)
temizle.place(x=890,y=930)

def clean():
    msg_box.delete(1, END)

def islem():
    yaz("....Başladı....")
    time.sleep(3)
    while True:
        while True:
            if pyautogui.pixel(850,942) [0] != 217:
                konum = str(pyautogui.position())
                konum_sliced = konum[6:19]
                konum_s = konum_sliced.split(",")
                x_sen = konum_s[0]
                y_sen = konum_s[1]
                x_s = x_sen.split("=")
                y_s = y_sen.split("=")
                x = int(x_s[1])
                y = int(y_s[1])
                pyautogui.doubleClick(434,938)
                pyautogui.click(434,938)
                pyautogui.hotkey("ctrl","c")
                win32clipboard.OpenClipboard()
                karsi_msg = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                pyautogui.moveTo(x,y)
                cevrilmis = translater.translate(karsi_msg,dest="tr",src="en")
                cevrilmis_txt = cevrilmis.text
                print(cevrilmis_txt)
                goruncek = f"O ---> {cevrilmis_txt.capitalize()}"
                msg_box.insert(END,"\n"+goruncek)
                yaz("..")
                time.sleep(2)
                break

def gonder():
    while True:
        time.sleep(0.001)
        if keyboard.is_pressed("enter") == True:
            send()
        else:
            time.sleep(0.001)

while keyboard.is_pressed('esc')==False:
    time.sleep(0.001)

threading.Thread(target=islem).start()
threading.Thread(target=gonder).start()

window.mainloop()
