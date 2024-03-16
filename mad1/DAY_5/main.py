from flask import Flask
from flask_restful import Api
from application.database import db

from application.model import *
import application.config as config
from application.api.TheaterAPI import TheaterAPI

app = Flask(__name__)
app.config.from_object(config)
app.app_context().push()

db.init_app(app)


api = Api(app)
api.init_app(app)


from application.controllers import *
from application.admin_controllers import *


api.add_resource(TheaterAPI, '/api/theater/<int:theater_id>',
                              '/api/theater')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000, debug=True)