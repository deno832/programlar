from flask import Flask
from views import views
import socket
import requests
import threading


app = Flask(__name__, static_folder='static')
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(host= "127.0.0.1" ,debug=True, port= 8000)