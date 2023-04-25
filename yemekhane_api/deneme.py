from fastapi import FastAPI , Response, status, HTTPException
from fastapi.params import Body
import sqlite3
from typing import Optional
from pydantic import BaseModel

class bilgiler(BaseModel):
    isim: str
    soy_isim: str
    numara: int
    hak: int
    sınıf: str
    id: str
    ödedi_mi: bool

class numara_deistir(BaseModel):
    numara: int
    yeni_hak: int

class id_deistir(BaseModel):
    id: str
    yeni_hak: int

class num_eksilt(BaseModel):
    numara: int


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "bşlangıç ekranı ez"}


@app.get("/cek/id/{id}")
def get_data(id):
    conn = sqlite3.connect("veri.db")
    c = conn.cursor()
    c.execute("SELECT * FROM ogrenciler WHERE id = ?",(id,))               #Kartın idsine göre öğrencinin bilgilerini çekmeye yarar.
    bilgi = c.fetchone()
    print(bilgi)
    conn.close()
    return {"isim": bilgi[0],"soy_isim":bilgi[1],
            "numara":bilgi[2],"hak":bilgi[3],"sınıf":bilgi[4],"id":bilgi[5],"ödedi_mi":bilgi[6]}


@app.get("/cek/numara/{num}")
def get_data(num):
    conn = sqlite3.connect("veri.db")
    c = conn.cursor()
    c.execute("SELECT * FROM ogrenciler WHERE numara = ?",(num,))       # Numaraya göre öğrenci bilgilerini çekmeye yarar.
    bilgi = c.fetchone()
    
    conn.close()
    
    try:
        return {"isim": bilgi[0],"soy_isim":bilgi[1],"numara":bilgi[2],"hak":bilgi[3],"sınıf":bilgi[4],"id":bilgi[5],"ödedi_mi":bilgi[6]}
    except:
        return Response(status_code= status.HTTP_404_NOT_FOUND)


@app.post("/ekle")
def kayıt_ekle(post: bilgiler):
    conn = sqlite3.connect("veri.db")
    c = conn.cursor()
    c.execute("INSERT INTO ogrenciler VALUES (?,?,?,?,?,?,?)",(post.isim, post.soy_isim, post.numara, post.hak, post.sınıf, post.id, post.ödedi_mi))   # Yeni bir öğrenciyi kaydetmeye yarar.
    conn.commit()
    conn.close()
    return {"message": "Kayıt Başarıyla Eklendi"}



@app.put("/deistir/numara")
def değiştir_num(post: numara_deistir):
    conn = sqlite3.connect("veri.db")
    c = conn.cursor()
    c.execute("UPDATE ogrenciler SET hak = ? WHERE numara= ?",(post.yeni_hak, post.numara))            # Bir öğrencinin hak sayısını numarası ile değiştirmeye yarar.
    conn.commit()
    conn.close()
    return {"message": f"{post.numara} numaralı öğrenicin hak sayısı {post.yeni_hak} olarak değiştirildi!"}



@app.put("/deistir/id")
def değiştir_id(post: id_deistir):
    conn = sqlite3.connect("veri.db")
    c = conn.cursor()
    c.execute("UPDATE ogrenciler SET hak = ? WHERE id= ?",(post.yeni_hak, post.id))     # Bir öğrencinin hak sayısını kart idsi ile değiştirmeye yarar.
    conn.commit()
    conn.close()
    return {"message": f"{post.id} uidli öğrenicin hak sayısı {post.yeni_hak} olarak değiştirildi!"}


@app.put("/eksilt/numara/{num}")
def eksilt_num(num):
    print("ADASDASDASD")
    conn = sqlite3.connect("veri.db")
    c = conn.cursor()
    c.execute("SELECT hak FROM ogrenciler WHERE numara = ?",(num,))
    hak = int(c.fetchone()[0])
    hak_eksi = hak - 1
    if hak > 0:
        c.execute("UPDATE ogrenciler SET hak = ? WHERE numara= ?",(str(hak_eksi), num))       # Numaraya göre kalan hakkının eksiltilmesine yarar.
        conn.commit()
        conn.close()
        return {"message": "Başarılı"}
    else:
        conn.close()
        return {"message": "Başarısız"}


@app.put("/eksilt/id/{id}")
def eksilt_num(id):
    conn = sqlite3.connect("veri.db")
    c = conn.cursor()
    c.execute("SELECT hak FROM ogrenciler WHERE id = ?",(id,))        # Kart idsine göre kalan hakkının eksiltilmesine yarar.
    hak = int(c.fetchone()[0])
    hak_eksi = hak - 1
    if hak > 0:
        c.execute("UPDATE ogrenciler SET hak = ? WHERE id= ?",(str(hak_eksi), id))
        conn.commit()
        conn.close()
        return {"message": "Başarılı"}
    else:
        conn.close()
        return {"message": "Başarısız"}
