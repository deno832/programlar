import socket
import threading
from tkinter import * 
from tkinter import messagebox
import pyautogui

def dewamke():
    global msg_box
    global nick
    global client_socket
    global entry

    nick = nick_entry.get()
    sifre = sifre_entry.get()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))
    print("Bağlandı")
    client_socket.send(f"/*-+<{nick}:{sifre}".encode())

    response = client_socket.recv(1024).decode()

    if response == "Başarılı":
        
        receive_thread = threading.Thread(target=receive_messages)
        receive_thread.start()
        pyautogui.alert(text=f"Giriş Yapılan Kullanıcı {nick}", title='Giriş Başarılı', button='OK')
        login.destroy()
        
    else:
        print("Başarısız Giriş!!")
        pyautogui.alert(text=f"Hatalı bilgi", title='Giriş Başarısız !!', button='OK')
        exit()
    
    window = Tk()
    window.title("Sohpet")
    window.geometry("600x850")
    window.resizable(False,False)

    msg_box = Text(window,height=30,width=60,font=("Arial",13))
    entry = Entry(window,width=67,font=("Arial",17))
    send_btn = Button(window,text="Gönder",font=("Arial",11),command=send)
    giris_yapan = Label(window,text=f"Giriş Yapılan Kullanıcı: {nick}",font=("Arial",12))

    msg_box.pack()
    entry.pack()
    send_btn.pack()
    giris_yapan.pack()

    window.mainloop()

def kaydol():
    nick = nick_entry.get()
    sifre = sifre_entry.get()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))
    client_socket.send(f"++--*/:{nick}:{sifre}".encode())
    response = client_socket.recv(1024).decode()
    
    if response == "Var":
        pyautogui.alert(text=f"Zaten Kayıtlı", title='Bu kullanıcı adı kullanılıyor! Bu yüzden kayıt olunamadı!', button='OK')
    elif response == "Kayıt Başarılı":
        pyautogui.alert(text=f"Kayıt Başarılı", title='Kayıt başarıyla oluşturuldu! Giriş yapabilirsiniz!', button='OK')
    else:
        pyautogui.alert(text=f"Hata", title='HATA!!!!!!!', button='NAPIM')
    register.destroy()

def send():
    global nick
    mesaj = entry.get()
    if mesaj != "":
        try:
            toSend = f"{nick} ----> {mesaj}".encode()
            msg_box.insert(END,"\n"+toSend.decode())
            entry.delete(0, END)
            client_socket.send(toSend)
            print("gönderildi!")
        except OSError:
            exit()
    else:
        pass

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            msg_box.insert(END,"\n"+message)
            print(message)
        except:
            client_socket.close()
            break

e_h = messagebox.askyesno("Hesap","Hesabınız var mı ?")

if e_h:
    login = Tk()
    login.geometry("260x320")
    login.title("Giriş Yap")
    login.resizable(False,False)
    baslık = Label(login,text="Girişi Yapma",font=("Arial",18)).pack()
    bos = Label(login).pack()

    nick_lbl = Label(login,font=("Arial",13),text="Kullanıcı Adı:").pack()
    nick_entry = Entry(login,font=("Arial",13))
    nick_entry.pack()
    sifre_lbl = Label(login,font=("Arial",13),text="Şifre:").pack()
    sifre_entry = Entry(login,font=("Arial",13))
    sifre_entry.pack()
    login_btn = Button(login,font=("Arial",14),text="Giriş Yap",command=dewamke).pack()
    login.mainloop()

else:
    register = Tk()
    register.geometry("260x320")
    register.title("Kayıt ol")
    register.resizable(False,False)
    baslık = Label(register,text="Kayıt Olma",font=("Arial",18)).pack()
    bos = Label(register).pack()

    nick_lbl = Label(register,font=("Arial",13),text="Kullanıcı Adı:").pack()
    nick_entry = Entry(register,font=("Arial",13))
    nick_entry.pack()
    sifre_lbl = Label(register,font=("Arial",13),text="Şifre:").pack()
    sifre_entry = Entry(register,font=("Arial",13))
    sifre_entry.pack()
    register_btn = Button(register,font=("Arial",14),text="Giriş Yap",command=kaydol).pack()
    register.mainloop()