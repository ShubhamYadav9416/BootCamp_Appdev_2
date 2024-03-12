from .database import db
from flask_security import UserMixin, RoleMixin

UserRole = db.Table('UserRoles',
                    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
                    db.Column('role_id', db.Integer, db.ForeignKey('role.id')))

class Role(db.Model,RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)


class User(db.Model,UserMixin):
    __table_name__ = 'user'
    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_mail = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable= False)
    active = db.Column(db.Boolean)

    fs_uniquifier = db.Column(db.String(250), unique=True, nullable=False)

    roles = db.relationship('Role',secondary= UserRole, backref=db.backref('user', lazy='dynamic'))
