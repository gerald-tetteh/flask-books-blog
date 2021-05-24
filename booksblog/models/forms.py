from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms.fields.core import BooleanField, StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_ckeditor import CKEditorField

class LoginForm(FlaskForm):
  email = StringField("Email", validators=[DataRequired(), Email()])
  password = PasswordField("Password", validators=[DataRequired()])
  remember_me = BooleanField("Remember Me")
  submit = SubmitField("Login")

class CreatePostForm(FlaskForm):
  title = StringField("Title", validators=[DataRequired()])
  imageUrl = StringField("Image Url", validators=[DataRequired()])
  description = CKEditorField("Content", validators=[DataRequired()])
  submit = SubmitField("Publish")