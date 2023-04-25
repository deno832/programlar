from flask import Blueprint, render_template
import socket

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

views = Blueprint(__name__, "views")
my_var = IPAddr

@views.route("/")
def home():
    return render_template("index.html", my_var=my_var)