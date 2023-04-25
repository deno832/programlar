from flask import Flask
from views import views
import socket

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)  

app = Flask(__name__, static_folder='static')
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(host= IPAddr ,debug=True, port= 8000)
