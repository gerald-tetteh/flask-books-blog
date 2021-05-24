from flask import Flask
from pymongo import MongoClient
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.config["SECRET_KEY"] = "621ce3fc-6aa9-4978-a4ec-6709008323e2"

login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
ckeditor = CKEditor(app)

login_manager.login_view = "login"
login_manager.login_message_category = "info"
client = MongoClient("mongodb+srv://admin:iykyUuJHSSDiy8Ps@cluster0.d93hs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["blog"]

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

from booksblog.routes import admin, blog