from flask_login import login_required, login_user, logout_user, current_user
from booksblog.models.user import User
from flask.helpers import url_for
from booksblog import app, db, bcrypt
from flask import render_template, redirect, flash
from booksblog.models.forms import CreatePostForm, LoginForm
from datetime import datetime

@app.route("/admin/login", methods=["GET","POST"])
def login():
  if current_user.is_authenticated:
    return redirect(url_for("index"))
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

@app.route("/admin/create-post", methods=["GET","POST"])
@login_required
def create_post():
  form =  CreatePostForm()
  if form.validate_on_submit():
    post = {
      "title": form.title.data,
      "imageUrl": form.imageUrl.data,
      "description": form.description.data,
      "date": datetime.utcnow()
    }
    db["posts"].insert_one(post)
    flash(f"Your post has been published","success")
    return redirect(url_for("index"))
  return render_template("admin/create_post.html", form=form, title="Create Post")