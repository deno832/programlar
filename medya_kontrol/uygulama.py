from fastapi import FastAPI , Response, status, HTTPException
import uvicorn
import win32api
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY, VK_VOLUME_UP, VK_VOLUME_DOWN, VK_MEDIA_NEXT_TRACK, VK_MEDIA_PREV_TRACK
import socket

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

app = FastAPI()

@app.get("/play-pause")
async def root():
    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)

@app.get("/arttir")
def arttir():
    win32api.keybd_event( VK_VOLUME_UP, 0, KEYEVENTF_EXTENDEDKEY, 0)

@app.get("/azalt")
def arttir():
    win32api.keybd_event( VK_VOLUME_DOWN, 0, KEYEVENTF_EXTENDEDKEY, 0)

@app.get("/sonraki")
def sonraki():
    win32api.keybd_event( VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)

@app.get("/önceki")
def sonraki():
    win32api.keybd_event( VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)

if __name__ == "__main__":
    uvicorn.run(app, host=IPAddr, port=4593)
