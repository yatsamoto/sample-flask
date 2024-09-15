from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # id, username, password
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(80), nullable=False, unique=True)
    password = db.Column(db.string(80), nullable=False)