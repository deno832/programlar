from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import threading
import subprocess
import os
import socket


filename = ""
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)  

window = Tk()
window.geometry("570x350")
window.title("Dosya Paylaşma Şeysi")

def klasör_seç():
    global filename
    filename = filedialog.askdirectory()
    print(filename)

def go_yerel():
    port = port_entry.get()
    try:
        os.chdir(filename)
    except OSError:
        messagebox.showerror("HATA!","Klasör Seçiniz!!")
        return 0
    subprocess.Popen(f"python -m http.server {port} -b {IPAddr}",shell=True)
    messagebox.showinfo("Adres",f"Yerel Ağda Bağlanmak İçin: https://{IPAddr}/{port}")

def tunnel(port,domain):
    print("srdsadads")
    os.chdir(filename)
    subprocess.Popen(f"npx localtunnel --port {port} --subdomain {domain}", shell= True)

    print("sdasda")
    messagebox.showinfo("Adress",f"Link: https://{domain}.loca.lt")


def go():
    port = port_entry.get()
    domain = domain_entry.get()
    threading.Thread(target=tunnel,args=(port,domain)).start()
    subprocess.Popen(f"python -m http.server {port} -b localhost",shell=True)


baslik = Label(window, text="Dosya Zımbırtısı",font=("Arial",18))
sec = Button(window, text="Klasör Seç", font=("Arial",15), command=klasör_seç)
domain_entry = Entry(window, font=("Arial",15))
port_entry = Entry(window, font=("Arial",15))
global_paylas = Button(window, text="Global Paylaş", command=go, font=("Arial",17))
yerel_paylas = Button(window, text="Yerel Paylaş", command=go_yerel, font=("Arial",17))
info = Label(window, text="(Yalnızca global paylaşım için!)",font=("Arial",9))

baslik.pack()
sec.place(x=215,y=50)
domain_entry.place(x=157,y=120)
domain_entry.insert(END,"Domain")
info.place(x=385,y=122)

port_entry.place(x=157,y=165)
port_entry.insert(END,"Port")
global_paylas.place(x=110,y=230)
yerel_paylas.place(x=280,y=230)

window.mainloop()