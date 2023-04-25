import cmath
import re
from tracemalloc import start
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import random
from tkinter import *
from PIL import Image,ImageTk
import webbrowser
from tkinter import messagebox
import win32clipboard
import keyboard
import pyautogui
from datetime import date 

# X: 755 Y: 919    RGB: (255, 255, 255)   yenimesaj
# X: 1586 Y:  921 RGB: (217, 253, 211)    bizim mesaj

driver = webdriver.Chrome(executable_path = r'C:\Users\Deniz\Documents\Python\selenium\chromedriver.exe')
driver.implicitly_wait(3)
driver.get("https://web.whatsapp.com/")

while keyboard.is_pressed('esc')==False:
    time.sleep(0.001)

message_area = driver.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
message_area.send_keys(".....Bot Başladı.....")
time.sleep(2)
send_btn = driver.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
send_btn.click()
time.sleep(1)

def yaz(msg):
    global driver
    message_area = driver.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    time.sleep(0.2)
    message_area.send_keys(msg)
    send_btn = driver.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    send_btn.click()


def kur(base,target):
    url = f"https://www.google.com/finance/quote/{base}-{target}?sa=X&ved=2ahUKEwiA05rHpf35AhWAQ_EDHYVHDvEQmY0JegQIBBAb"

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,"html.parser")
    title = soup.find("div", {"class": "YMlKec fxKbKc"})
    rate = title.get_text()
    return rate

def duzelt(kelime):
    url = f"https://www.google.com/search?q={kelime}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    try:
        titl = soup.find("a", class_="gL9Hy").get_text().strip()
        return titl
    except:
        return "HATA"

while True:
    while True:
        time.sleep(0.2)
        if pyautogui.pixel(1586,921) [0] != 217 :
            time.sleep(0.2)
            pyautogui.doubleClick(755,919)
            pyautogui.click(755,919)
            pyautogui.hotkey("ctrl","c")
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            print(data.capitalize())
            if "Selam" == data or "Nasılsın"== data or "İyi misin" == data:
                yaz("İyiyim sen nasılsın?")
            elif "Merhaba" == data:
                yaz("Merhabana merhaba gardaş!")
            elif "Mal" == data:
                yaz("Sensin mal!!")
            elif "Hayat nasıl" == data:
                yaz("İyi gidiyor,seninki?")
            elif "Bana şarkı söyle" == data:
                yaz("Sesim çok robotik,yoksa söylerdim tabii.")
            elif "Ne yapıyorsun" == data:    
                yap = ["Yıldızlararası Yolculuktayım","Robot çiçeklerimi suluyorum","Kodumu güncellemekle meşgulüm.","Kendime işlemci bakıyorum"]
                yaz(random.choice(yap))
            elif "Hangi takımlısın" == data or "Hangi takımı tutuyorsun" == data or "Hangi takımı destekliyorsun" == data or "En iyi takım hangisi" == data:
                yaz("Sonsuza Kadar GALATASARAY!!!")
            elif "Çarpma yap" == data:
                flag = True
                yaz("Çarpmam gereken ilk sayıyı yaz.")
                while True:
                    time.sleep(0.1)
                    if pyautogui.pixel(1586,921) [0] != 217 :
                        if flag == False :
                            break
                        pyautogui.doubleClick(755,919)
                        pyautogui.click(755,919)
                        pyautogui.hotkey("ctrl","c")
                        win32clipboard.OpenClipboard()
                        data = win32clipboard.GetClipboardData()
                        win32clipboard.CloseClipboard()
                        sayi_1 = int(data)
                        yaz(f"İlk sayın: {sayi_1}")
                        time.sleep(1)
                        yaz("Çarpmam gereken ikinci sayıyı yaz.")
                        while True:
                            time.sleep(0.1)
                            if pyautogui.pixel(1586,921) [0] != 217 :
                                pyautogui.doubleClick(755,919)
                                pyautogui.click(755,919)
                                pyautogui.hotkey("ctrl","c")
                                win32clipboard.OpenClipboard()
                                data = win32clipboard.GetClipboardData()
                                win32clipboard.CloseClipboard()
                                sayi_2 = int(data)
                                sonuc = sayi_1 * sayi_2
                                yaz(f"İkinci sayın:{sayi_2}")
                                yaz(f"Çarpım sonucun:{sonuc}")
                                flag = False
                                break
            elif "Dolar kaç" == data or "Dolar" == data:
                dolar =kur("USD","TRY")
                sent = f"1 Dolar = {dolar} TL"
                yaz(sent)
            elif "Euro kaç" == data or "Euro" == data or "euro" == data:
                euro = kur("EUR","TRY")
                sent = f"1 Euro = {euro} TL"
                yaz(sent)
            elif "Btc" == data or "Bitcoin" == data or "BTC" ==data or "Bitcoin kaç" == data or "Coin kaç oldu" == data:
                btc_TRY = kur("BTC","TRY")
                sent_try = f"1 Bitcoin = {btc_TRY} TRY"
                yaz(sent_try)
                btc_USD = kur("BTC","USD")
                sent_USD = f"1 Bitcoin = {btc_USD} USD"
                yaz(sent_USD)
            elif "ETH" == data or "Etherium" == data or "ETH kaç" == data or "Eth" == data:
                eth_TRY = kur("ETH","TRY")
                sent_TRY = f"1 Etherium = {eth_TRY} TRY"
                yaz(sent_TRY)
                eth_USD = kur("ETH","USD")
                sent_USD = f"1 Etherium = {eth_USD} USD"
                yaz(sent_USD)
            elif "Tarih" == data or "Ayın kaçı" == data:
                today = date.today()
                yaz("Bugünün Tarihi:",today)
            elif "Saat" == data or "Saat kaç" == data:
                yaz(time.strftime("%H:%M:%S"))

            
            else:
                data = duzelt(data)
                if data == "HATA":
                    yaz("Ben henüz cahilim./HATA!")
                elif "Selam" == data or "Nasılsın"== data or "İyi misin" == data:
                    yaz("İyiyim sen nasılsın?")
                elif "Merhaba" == data:
                    yaz("Merhabana merhaba gardaş!")
                elif "Mal" == data:
                    yaz("Sensin mal!!")
                elif "Hayat nasıl" == data:
                    yaz("İyi gidiyor,seninki?")
                elif "Bana şarkı söyle" == data or "Şarkı söyle" == data:
                    yaz("Sesim çok robotik,yoksa söylerdim tabii.")
                elif "Ne yapıyorsun" == data:    
                    yap = ["Yıldızlararası Yolculuktayım","Robot çiçeklerimi suluyorum","Kodumu güncellemekle meşgulüm.","Kendime işlemci bakıyorum"]
                    yaz(random.choice(yap))
                elif "Hangi takımlısın" == data or "Hangi takımı tutuyorsun" == data or "Hangi takımı destekliyorsun" == data or "En iyi takım hangisi" == data:
                    yaz("Sonsuza Kadar GALATASARAY!!!")
                elif "Çarpma yap" == data:
                    flag = True
                    yaz("Çarpmam gereken ilk sayıyı yaz.")
                    while True:
                        time.sleep(0.1)
                        if pyautogui.pixel(1586,921) [0] != 217 :
                            if flag == False :
                                break
                            pyautogui.doubleClick(755,919)
                            pyautogui.click(755,919)
                            pyautogui.hotkey("ctrl","c")
                            win32clipboard.OpenClipboard()
                            data = win32clipboard.GetClipboardData()
                            win32clipboard.CloseClipboard()
                            sayi_1 = int(data)
                            yaz(f"İlk sayın: {sayi_1}")
                            time.sleep(1)
                            yaz("Çarpmam gereken ikinci sayıyı yaz.")
                            while True:
                                time.sleep(0.1)
                                if pyautogui.pixel(1586,921) [0] != 217 :
                                    pyautogui.doubleClick(755,919)
                                    pyautogui.click(755,919)
                                    pyautogui.hotkey("ctrl","c")
                                    win32clipboard.OpenClipboard()
                                    data = win32clipboard.GetClipboardData()
                                    win32clipboard.CloseClipboard()
                                    sayi_2 = int(data)
                                    sonuc = sayi_1 * sayi_2
                                    yaz(f"İkinci sayın:{sayi_2}")
                                    yaz(f"Çarpım sonucun:{sonuc}")
                                    flag = False
                                    break
                elif "Dolar kaç" == data or "Dolar" == data:
                    dolar =kur("USD","TRY")
                    sent = f"1 Dolar = {dolar} TL"
                    yaz(sent)
                elif "Euro kaç" == data or "Euro" == data or "euro" == data:
                    euro = kur("EUR","TRY")
                    sent = f"1 Euro = {euro} TL"
                    yaz(sent)
                elif "Btc" == data or "Bitcoin" == data or "BTC" ==data or "Bitcoin kaç" == data or "Coin kaç oldu" == data:
                    btc_TRY = kur("BTC","TRY")
                    sent_try = f"1 Bitcoin = {btc_TRY} TRY"
                    yaz(sent_try)
                    btc_USD = kur("BTC","USD")
                    sent_USD = f"1 Bitcoin = {btc_USD} USD"
                    yaz(sent_USD)
                elif "ETH" == data or "Etherium" == data or "ETH kaç" == data or "Eth" == data:
                    eth_TRY = kur("ETH","TRY")
                    sent_TRY = f"1 Etherium = {eth_TRY} TRY"
                    yaz(sent_TRY)
                    eth_USD = kur("ETH","USD")
                    sent_USD = f"1 Etherium = {eth_USD} USD"
                    yaz(sent_USD)
                elif "Saat" == data or "Saat kaç" == data:
                    yaz(time.strftime("%H:%M:%S"))
                else:
                    yaz("Düzeltmeye rağmen cahilim")
                    break
