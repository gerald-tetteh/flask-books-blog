from flask_login import UserMixin
from booksblog import login_manager, db
from bson.objectid import ObjectId

@login_manager.user_loader
def load_user(user_id):
  db_user = db["users"].find_one({"_id": ObjectId(user_id)})
  return User(db_user["_id"],db_user["email"],db_user["password"])

class User(UserMixin):
  def __init__(self,id,email,password) -> None:
    super().__init__()
    self.id = id
    self.email = email
    self.password = password
  
  def __repr__(self) -> str:
    return f"User('{self.email}','{self.password}')"