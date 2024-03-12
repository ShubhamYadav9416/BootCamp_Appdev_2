from flask import jsonify

from flask_restful import Resource, reqparse,abort

from flask_security import verify_password,login_user
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity


from application.data.model import db,User,Role, UserRole



login_parser = reqparse.RequestParser()
login_parser.add_argument('user_mail', type=str, required=True, help="User mail is required")
login_parser.add_argument('password', type=str, required=True, help="Password is required")

class LoginAPI(Resource):
    def post(resource):
        args = login_parser.parse_args()
        user_mail = args.get('user_mail')
        password = args.get('password')

        if "@" not in args["user_mail"]:
            abort(409, message="user mail is not mail")

        user = User.query.filter_by(user_mail = user_mail).first()
        if not user:
            return jsonify({'status':'failed','message':'Mail is not registered!!'})
        
        if verify_password(password, user.password):
            return jsonify({'status':'failed', 'message':'wrong password'})
        
        refresh_token = create_refresh_token(identity=user.user_id)
        access_token = create_access_token(identity=user.user_id)

        login_user(user)

        return jsonify({'status':'success', 'message':'successfully logined in !!!',
                        'access_token':access_token, 'refresh_token':refresh_token})
    

class RefreshTokenAPI(Resource):
    @jwt_required(refresh=True)
    def post(resource):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return {'access_token': access_token}, 200

