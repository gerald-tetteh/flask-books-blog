from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://admin:mNtP08nDelAwJQD@cluster0.d93hs.mongodb.net/")
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