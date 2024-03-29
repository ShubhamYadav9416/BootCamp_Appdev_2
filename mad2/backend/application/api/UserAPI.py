from flask import request, jsonify
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from flask_jwt_extended import jwt_required, get_jwt_identity
from time import perf_counter_ns

from application.data.model import db, User
from application.data.data_access import get_all_users

user_post_args = reqparse.RequestParser()
user_post_args.add_argument('user_mail', type=str, required = True, help="user mail is required")
user_post_args.add_argument('password', type=str, required = True, help="password is required")

user_put_args = reqparse.RequestParser()
user_put_args.add_argument('user_mail', type=str)
user_put_args.add_argument('password', type=str)


resource_fields ={
    'user_id': fields.Integer,
    'user_mail': fields.String,
    'password': fields.String
}

class UserAPI(Resource):
    @jwt_required()
    @marshal_with(resource_fields)
    def get(self, user_id):
        user = User.query.filter_by(user_id = user_id).first()
        if not user:
            abort(404, messasge= "no user exist with this user_id")
        return user

    @jwt_required()
    def delete(self,user_id):
        user = User.query.filter_by(user_id = user_id).first()
        if not user:
            abort(404, messasge= "no user exist with this user_id")
        db.session.delete(user)
        db.session.commit()
        return jsonify({'status': "success", 'message': 'user is deleted'})

    @jwt_required()
    @marshal_with(resource_fields)
    def put(self,user_id):
        args = user_put_args.parse_args()
        user = User.query.filter_by(user_id = user_id).first()
        if not user:
            abort(404, messasge= "no user exist with this user_id")
        if args["user_mail"]:
            user.user_mail = args["user_mail"]
        if args["password"]:
            user.password = args["password"]
        db.session.commit()
        return user



class AllUserAPI(Resource):
    @jwt_required()
    def get(resource):
        start = perf_counter_ns()
        all_user = get_all_users()
        stop = perf_counter_ns()
        print(stop-start)
        return all_user


        # users = User.query.all()
        # all_user = []
        # for user in users:
        #     all_user.append({'user_id': user.user_id,
        #                      'user_mail': user.user_mail,
        #                      'password': user.password})
        # return all_user

    @jwt_required()
    def post(resource):
        args = user_post_args.parse_args()
        user = User.query.filter_by(user_mail = args["user_mail"]).first()
        if "@" not in args["user_mail"]:
            abort(409, message="user mail is not mail")
        if user:
            abort(409, message="user mail already exists")
        input =  User(user_mail = args['user_mail'], password = args["password"])
        db.session.add(input)
        db.session.commit()
        return "user is registerd", 200
