from flask import Flask
from application.database import db
from application.model import *
import application.config as config

app = Flask(__name__)
app.config.from_object(config)
app.app_context().push()

db.init_app(app)


from application.controllers import *


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000, debug=True)