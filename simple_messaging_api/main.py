import sqlite3
import uvicorn
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import datetime
from functions import *
from starlette import status
from starlette.responses import JSONResponse

class user(BaseModel):   # Kullanıcı modelini oluşturma
    nickname: str
    password: str
    mail_adress: str

class login_user(BaseModel):   # Kullanıcı modelini oluşturma
    nickname: str
    password: str

class message(BaseModel):   # Kullanıcı modelini oluşturma
    nickname: str
    password: str
    
class send_message(BaseModel):
    username: str
    password: str
    reciever_id: int
    message_content: str

class get_msgs_model(BaseModel):
    username: str
    password: str
    wanted_person: str


app = FastAPI()

@app.get("/")
def root():
    return {"message": "HO"}

@app.get("/get_user_id/{nickname}")
def get_id(nickname):
    return {"response": get_user_id(nickname)}

@app.post("/register")   # Kullanıcı kaydı talebini tanımlama
def kayıt(post: user):

    is_exists = check_if_exists(post.nickname)
    if not is_exists:
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users(nickname, password, mail_adress) VALUES (?,?,?)", (post.nickname, post.password, post.mail_adress))
            conn.commit()
            conn.close()
            return {"message" : "ok"}
        except:
            return JSONResponse(content={"message" : "error"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return {"message" : "Username Already Exists!"}

@app.post("/login")
def login(post: login_user):
    isMatch = check_credentials(post.nickname, post.password)
    
    if not isMatch:
        return JSONResponse(content={"message": "Invalid credentials!"}, status_code=status.HTTP_401_UNAUTHORIZED)

    else:
        return {"message": "Succesfull login!","id": isMatch}

@app.post("/send_message")
def send(post: send_message):
    sender_id = check_credentials(post.username, post.password)
    
    if not sender_id:
        return JSONResponse(content={"message": "Invalid credentials!"}, status_code=status.HTTP_401_UNAUTHORIZED)

    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages(sender_id, receiver_id, message_text, date) VALUES (?,?,?,?)", (sender_id, post.reciever_id, post.message_content, datetime.datetime.now()))
    conn.commit()
    conn.close()
    return {"message": "Success"}

@app.post("/get_messages")
def get_msgs(post: get_msgs_model):
    sender_id = check_credentials(post.username, post.password)

    if not sender_id:
        return JSONResponse(content={"message": "Invalid credentials!"}, status_code=status.HTTP_401_UNAUTHORIZED)

    other_id = get_user_id(post.wanted_person)

    messages = get_messages_by_id(other_id, sender_id)
    return {"response": messages}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
