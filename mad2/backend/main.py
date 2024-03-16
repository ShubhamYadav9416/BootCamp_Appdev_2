from flask import Flask
from flask_restful import Api

import application.config as config
from application.data.database import db
from application.data.model import *
from application.cache import cache

from application.security import user_datastore, security
from flask_jwt_extended import JWTManager
from flask_cors import CORS


from application.api.UserAPI import AllUserAPI, UserAPI
from application.api.auth.registerAPI import RegisterAPI
from application.api.auth.loginAPI import LoginAPI, RefreshTokenAPI


app = Flask(__name__)
app.config.from_object(config)
app.app_context().push()


CORS(app, supports_credentials=True)

# Add CORS headers to every response-----------------
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, POST, DELETE, OPTIONS'

    return response

@app.after_request
def after_request(response):
    response = add_cors_headers(response)
    return response




db.init_app(app)

api = Api(app)
api.init_app(app)

JWTManager(app)

security.init_app(app, user_datastore)

cache.init_app(app)

api.add_resource(AllUserAPI, "/api/user")
api.add_resource(UserAPI, "/api/user/<int:user_id>")
api.add_resource(RegisterAPI, '/api/user/register')
api.add_resource(LoginAPI, '/api/user/login')
api.add_resource(RefreshTokenAPI, '/api/user/refresh_token')




def create_roles_init():
    if Role.query.filter_by(name='admin').first() is None:
        new_role =  Role(name='admin')
        db.session.add(new_role)
        db.session.commit()
    if Role.query.filter_by(name='user').first() is None:
        new_role =  Role(name='user')
        db.session.add(new_role)
        db.session.commit()
    



with app.app_context():
    db.create_all()
    create_roles_init()






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)