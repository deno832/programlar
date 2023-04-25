from flask import Blueprint, render_template
import socket
import requests
from flask import request


hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

views = Blueprint(__name__, "views")
my_var = IPAddr

@views.route("/")
def home():
    return render_template("login.html")

@views.route('/dashboard/<token>', methods=['GET'])
def dashboard(token):
    print(token)
    response = requests.get(f"http://say-clusters.at.ply.gg:2395/is_exists/{token}").json()

    if response["message"] == True:
        return render_template("menu.html", my_var=token)
    else:
        return "<h1>Geçersiz Token!!! Tekrar Giriş Yapmayı Dene</h1>"