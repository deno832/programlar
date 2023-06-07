import socket
import os
import subprocess
from tkinter import *


hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

window = Tk()
window.geometry("600x140")
window.title("Medya Kontrol")

lbl = Label(window,text=f"Bu linke bağlanın: http://{IPAddr}:8000",font=("Arial",19))
lbl.place(relx=.5, rely=.5, anchor="center")



subprocess.Popen(f"python app.py", shell= True)
subprocess.Popen(f"python uygulama.py", shell= True)

print(f"Bu linke bağlanın: http://{IPAddr}:8000/views")

window.mainloop()