from .database import db


class User(db.Model):
    __table_name__ = 'user'
    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_mail = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable= False)
