from flask import Flask
from views import views
import cv2

app = Flask(__name__, static_folder='static')
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(host= "127.0.0.1", port= 8000)