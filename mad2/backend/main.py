from flask import Flask
from flask_restful import Api

import application.config as config
from application.data.database import db
from application.data.model import *


from application.api.UserAPI import AllUserAPI, UserAPI


app = Flask(__name__)
app.config.from_object(config)
app.app_context().push()


db.init_app(app)

api = Api(app)
api.init_app(app)

api.add_resource(AllUserAPI, "/api/user")
api.add_resource(UserAPI, "/api/user/<int:user_id>")

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)