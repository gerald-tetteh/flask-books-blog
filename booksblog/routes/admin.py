from flask_login.utils import login_user, logout_user
from booksblog.models.user import User
from flask.helpers import url_for
from booksblog import app, db, bcrypt
from flask import render_template, redirect, flash
from booksblog.models.forms import LoginForm

@app.route("/admin/login", methods=["GET","POST"])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    db_user = db["users"].find_one({"email": form.email.data})
    if db_user and bcrypt.check_password_hash(db_user["password"],form.password.data):
      user = User(db_user["_id"],db_user["email"],db_user["password"])
      login_user(user,remember=form.remember_me.data)
      flash(f"You have been signed in","success")
      return redirect(url_for("index"))
    else:
      flash(f"Login unsuccessful. Please check your email and password", "danger")
  return render_template("admin/login.html", form=form, title="Admin")

@app.route("/admin/logout")
def logout():
  logout_user()
  return redirect(url_for("index"))