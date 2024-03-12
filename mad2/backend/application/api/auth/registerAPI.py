from flask import jsonify
from flask_restful import Resource, reqparse, abort
from werkzeug.security import generate_password_hash
import secrets


from application.data.model import db, User, Role

user_post_args =  reqparse.RequestParser()
user_post_args.add_argument('user_mail', type=str, required=True, help="User mail is required")
user_post_args.add_argument('password', type=str, required=True, help="Password is required")


class RegisterAPI(Resource):
    def post(resource):
        args = user_post_args.parse_args()
        user_mail = args.get('user_mail')
        password = args.get('password')

        if "@" not in args["user_mail"]:
            abort(409, message="user mail is not mail")

        user = User.query.filter_by(user_mail = user_mail).first()
        if user:
            return jsonify({'status':'failed','message':'Mail is already registered!!'})
        
        hashed_password = generate_password_hash(password)

        new_user = User(user_mail=user_mail, password=hashed_password, active=True)
        new_user.fs_uniquifier = secrets.token_hex(16)
        
        role = Role.query.filter_by(name='user').first()

        new_user.roles.append(role)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'status': 'success', 'message': 'Successfully Regsitered!!'})
