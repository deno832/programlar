from fastapi import FastAPI , Response, status, HTTPException
import uvicorn
import socket
from pydantic import BaseModel
import sqlite3
from fastapi.middleware.cors import CORSMiddleware
import random
import threading
import time
import subprocess
import os
from mctools import RCONClient
import shutil


HOST = '127.0.0.1'  # Hostname of the Minecraft server
PORT = 12345  # Port number of the RCON server

rcon = RCONClient(HOST, port=PORT)

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

tokens = [1]

class login(BaseModel):
    first_name: str
    password: str

class rcon_model(BaseModel):
    token: int
    command: str

class get_token(BaseModel):
    token: int

class send_prop(BaseModel):
    token: int
    file: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
def login(data: login):
    conn = sqlite3.connect("veri.db")
    c = conn.cursor()
    try:
        c.execute("SELECT password FROM users WHERE first_name = ?",(data.first_name,))
        gercek_sifre = c.fetchone()[0]
        conn.close()
    except:
        return {"message": "Kullanıcı yok"}
    
    if data.password == gercek_sifre:
        new_token = random.randint(0,1000000000000)
        
        tokens.append(new_token)
        
        return {'message': "Başarılı giriş", "token": new_token}
    else:
        return {'message': "Şifre yanlış"}

@app.get("/is_exists/{token}")
def exists(token):
    if int(token) in tokens:
        return {"message": True}
    else:
        return {"message":False}

@app.get("/start/{token}")
def start(token):
    if int(token) in tokens:
        if process_exists("java.exe") == False:
            os.chdir(r"C:\Users\Deniz\Documents\mc-server-python\api\server")
            subprocess.Popen(["start", "cmd", "/k", r"C:\Users\Deniz\Documents\mc-server-python\api\server\server.jar"], shell = True)
            return {"message": "Başlatıldı"} 
        else:
            return {"message": "Çalışıyor"} 
    else:
        return {"message":False}

@app.post("/send-command")
def command(data: rcon_model):
    if data.token in tokens:
        print(process_exists("javaw.exe"))
        if process_exists("javaw.exe") == True:
            if rcon.login("supersekret"):
                if data.command == "stop":
                    rcon.command("stop")
                    resp = rcon.stop()
                    return {"command_out": str(resp)[:-4]}
                resp = rcon.command(data.command)
                
                print(str(resp))
                return {"command_out": str(resp)[:-4]}
            else:
                return {"command_out": "Login err"}
        else:
            return {"command_out": "Server inactive"}
    else:
        return {"command_out": "Token not valid"}

@app.post("/get-prop")
def get_tokenads(data: get_token):
    if data.token in tokens:
        if process_exists("java.exe") == True:
            return {"message": "Sunucu çalışıyor.."}
        with open(r"C:\Users\Deniz\Documents\mc-server-python\api\server\server.properties", "r") as f:
            content = f.read()
            f.close()
        return {"message": content}
        
@app.post("/send-prop")
def send_proper(data: send_prop):
    if data.token in tokens:
        with open(r"C:\Users\Deniz\Documents\mc-server-python\api\server\server.properties", "w") as f:
            f.write(data.file)
            f.close()
        return {"message": "succes"}

@app.get("/is-running/{token}")
def start(token):
    if int(token) in tokens:
        if process_exists("java.exe") == True:
            return {"message": True}
        else:
            return {"message": False}
    else:
        return {"message": "izin yok"}

@app.get("/reset-settings/{token}")
def reset(token):
    if int(token) in tokens:
        if process_exists("java.exe") == False:
            os.remove(r"C:\Users\Deniz\Documents\mc-server-python\api\server\server.properties")
            time.sleep(0.1)
            shutil.copy2(r"C:\Users\Deniz\Documents\mc-server-python\api\server.properties",r"C:\Users\Deniz\Documents\mc-server-python\api\server")
            return {"message":"Success"}
        else:
            return {"message":"Çalışıyor"}

# def token_func():
#     global tokens
#     time.sleep(120)
#     tokens = []

# threading.Thread(target=token_func).start()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=800)