from flask_security import Security, SQLAlchemySessionUserDatastore
from .data.model import db, User, Role

user_datastore = SQLAlchemySessionUserDatastore(db,User, Role)

security = Security()