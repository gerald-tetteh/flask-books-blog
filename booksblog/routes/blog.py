from flask import url_for
from flask.templating import render_template
from booksblog import app

@app.route("/")
@app.route("/home")
def index():
  return render_template("blog/index.html", title="Books Blog - Criss Nellaer")