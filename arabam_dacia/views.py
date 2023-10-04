from flask import Blueprint, render_template, Response
import socket
import cv2

views = Blueprint(__name__, "views")
my_var = "Arabaam he arabaam"

my_var = input("Link giriniz: ")

def func():
    while True:
        succes,frame = camera.read()

        # scale_percent = 40
        # width = int(framee.shape[1] * scale_percent * 100)   
        # height = int(framee.shape[0] * scale_percent * 100)
        
        # dim = (width,height)
        # frame = cv2.resize(framee, dim, interpolation = cv2.INTER_AREA)
        # print("frameeeeeee")

        if not succes:
            break
        else:
            ret,buffer = cv2.imencode(".jpg",frame)
            frame = buffer.tobytes()
        
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@views.route("/")
def home():
    return render_template("index.html", my_var=my_var)

# @views.route("/video")
 # def video():
  #  return Response(func(),mimetype="multipart/x-mixed-replace; boundary=frame")
