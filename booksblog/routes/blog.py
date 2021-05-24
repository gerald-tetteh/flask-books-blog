from flask import url_for
from flask.templating import render_template
from booksblog import app, db

@app.route("/")
@app.route("/home")
def index():
  posts = db["posts"].find().sort("date")
  return render_template("blog/index.html", title="Books Blog - Criss Nellaer", posts=posts)