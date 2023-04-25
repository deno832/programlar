import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
import random
import os
from playsound import playsound
import serial.tools.list_ports
import threading
import urllib.request
import re
from googletrans import Translator
import requests
from bs4 import BeautifulSoup

translater = Translator()

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

r = sr.Recognizer()
konuşun = r"C:\\Users\Deniz\Documents\\Python\\oda_serial_ardu\\asistan\\crystal.wav"
alarm = r"C:\\Users\Deniz\Documents\\Python\\oda_serial_ardu\\asistan\\alarm.wav"
bitti = r"C:\\Users\Deniz\Documents\\Python\\oda_serial_ardu\\asistan\\bitti.wav"

def get_video_duration(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    duration_meta = soup.find("meta", attrs={"itemprop": "duration"})
    if duration_meta:
        duration = duration_meta["content"]
        duration = duration[2:]   #7M7S
        duration = duration.replace("S","")   #7M7
        duration = duration.split("M")
        seconds = (int(duration[0]) * 60) + int(duration[1])
        return seconds
    else:
        return None

def yt(string):
    search_keyword = string
    search_keyword = search_keyword.replace(" ","_")
    search_keyword = search_keyword.replace("ı","i")
    search_keyword = search_keyword.replace("ğ","g")
    search_keyword = search_keyword.replace("ç","c")
    search_keyword = search_keyword.replace("ş","s")
    print(search_keyword)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = "https://www.youtube.com/watch?v=" + video_ids[0]
    return url

def record():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=5)
        print("Konuşun")
        playsound(konuşun)
        audio = r.listen(source)
        print("Bitti")
        playsound(bitti)
        voice = ""
        try:
            voice = r.recognize_google(audio , language = "tr-TR")
        except sr.UnknownValueError:
            speak("Anlayamadım")
            print("Anlayamadım")
        except sr.requestError:
            speak("Sistem çalışmıyor")
        return voice.capitalize()

def record_eng():
    with sr.Microphone() as source:
        print("Konuşun")
        playsound(konuşun)
        audio = r.listen(source)
        print("Bitti")
        playsound(bitti)
        voice = ""
        try:
            voice = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Anlayamadım")
            print("Anlayamadım")
        except sr.requestError:
            speak("Sistem çalışmıyor")
        return voice.capitalize()

def response(voice):
    if "Nasılsın" in voice:
        speak("İyiyim Sen Nasılsın?")
        print("İyiyim sen Nasılsın?")
        mood = record()
        print(mood)
        if "İyiyim" or "Süperim "or "Bomba gibiyim" in mood:
            speak("İyi olmana sevindim!")
            print("İyi olmana sevindim!")
        elif "Kötüyüm" or "Berbatım" or "İyi değilim" or "İyi değilim" in mood:
            speak("Kötü olmana üzüldüm!")
            print("Kötü olmana üzüldüm!")
    if "Saat kaç" in voice:
        speak(datetime.now().strftime("%H:%M"))
        print(datetime.now().strftime("%H:%M"))
    if "Arama yap" in voice:
        speak("Ne aramak istiyorsun ?")
        print("Ne aramak istiyorsun?")
        search = record()
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        speak(search + " İçin bulduklarım :")
    if "Tamamdır" in voice:
        speak("Görüşürüz")
        exit()
    if "Video ara" in voice:
        speak("Ne aramak istiyorsun ?")
        print("Ne aramak istiyorsun?")
        search = record()
        url = "https://www.youtube.com/results?search_query=" + search
        webbrowser.get().open(url)
        speak(search + "İçin YouTube'da bulduklarım")
    if "Arama motorunu aç" in voice:
        webbrowser.open("https://www.google.com.tr")
    if "Instagram'ı aç" in voice:
        webbrowser.open("https://www.instagram.com/?hl=tr")
    if "İngilizce çeviri yap" in voice:
        speak("Neyi türkçeye çevirmemi istiyorsun?")
        print("Neyi türkçeye çevirmemi istiyorsun?")
        search = record_eng()
        print(search)
        out = translater.translate(search,dest="tr",src="en")
        out = out.text
        speak(f"Söylediğiniz kelime {out} anlamına gelir")
    if "Eş anlamlısını bul" in voice:
        speak("Neyin eş anlamlısını bulmamı istiyorsun?")
        print("Neyin eş anlamlısını bulmamı istiyorsun?")
        url = "https://es-anlam.com/kelime/" + record()
        headerss = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
        page = requests.get(url,headers=headerss)
        soup = BeautifulSoup(page.content,"html.parser")
        title = soup.find(id="esanlamlar").get_text().strip()
        speak(title)
    if "Zıt anlamlısını bul" in voice:
        speak("Neyin zıt anlamlısını bulmamı istiyorsun?")
        print("Neyin zıt anlamlısını bulmamı istiyorsun?")
        search = record()
        url = "https://www.es-anlam.com/zit-anlam/kelime/" + search
        headerss = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
        page = requests.get(url,headers=headerss)
        soup = BeautifulSoup(page.content,"html.parser")
        title = soup.find(id="esanlamlar").get_text().strip()
        speak(title)
    if "Zamanlayıcı kur" in voice:
        speak("Kaç dakika sonrasına kurmamı istiyorsun ?")
        print("Kaç dakika sonrasına kurmamı istiyorsun ?")
        dakika = record()
        print(dakika)
        saniye = int(dakika) * 5
        geçen = 0
        while geçen < saniye:
            time.sleep(1)
            print(geçen)
            geçen += 1
            if geçen % 5 == 0:
                speak(f"{geçen/5} dakika kaldı")
                geçen += 3
        playsound(alarm)
        time.sleep(4)
        speak("Alarm çaldı!!")
    if "Işığı aç" in voice:
        serialInst.write(str.encode("ac\r\n"))
        speak("Işık açıldı!")
    if "Işığı kapat" in voice:
        serialInst.write(str.encode("kapa\r\n"))
        speak("Işık kapatıldı!")
    if "Ders çalışma müziği aç" in voice:
        webbrowser.open("")
    if "Youtube'da türkçe çal" in voice:
        speak("Ne çalayım?")
        wordd = record()
        link = yt(wordd)
        webbrowser.open(link, new=1, autoraise=True)
        sn = get_video_duration(link)
        threading.Thread(target=sure_bekle,args=(sn,)).start()
        
    if "Youtube'da i̇ngilizce çal" in voice:
        speak("Ne çalayım?")
        wordd = record_eng()
        webbrowser.open(yt(wordd))

def speak(string):
    tts = gTTS(string,lang="tr")
    rand = random.randint(1,10000)
    file = "audio-" + str(rand) + ".mp3"
    tts.save(file)
    time.sleep(1)
    playsound(file)
    time.sleep(6)
    os.remove(file)

def sure_bekle(sure):
    a = 0
    time.sleep(sure+5)
    print("Betteeee!!")
    os.system("TASKKILL /F /IM chrome.exe")


def speak_eng(string):
    tts = gTTS(string,lang="en")
    rand = random.randint(1,10000)
    file = "audio-" + str(rand) + ".mp3"
    tts.save(file)
    time.sleep(1)
    playsound(file)
    time.sleep(6)
    os.remove(file)

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        cardn = packet.decode("utf").rstrip("\n")
        cardr = cardn.rstrip("\r")
        card = cardr.rstrip(" ")
        print(card)
        if card == "basla":
            speak("Nasıl yardımcı olabilirim?")
            voice = record()
            print(voice)
            response(voice)