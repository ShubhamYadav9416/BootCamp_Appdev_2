from flask_restful import Resource, marshal_with, abort,fields,reqparse
from flask import  jsonify

from application.model import Theater, db

resource_fields={
    "theater_id": fields.Integer,
    "theater_name":fields.String,
    "place": fields.String,
    "location":fields.String,
    "capacity":fields.Integer,
    "rating":fields.Float
}

theater_post_args = reqparse.RequestParser()
theater_post_args.add_argument('theater_name', type=str, required = True, help="theater name is not here")
theater_post_args.add_argument('place', type = str, required = True, help="theater name is not here")
theater_post_args.add_argument('location', type = str, required = True, help="theater name is not here")
theater_post_args.add_argument('capacity', type = int, required = True, help="theater name is not here")
theater_post_args.add_argument('rating', type = float, required = True, help="theater name is not here")

theater_put_args = reqparse.RequestParser()
theater_put_args.add_argument('theater_name', type=str)
theater_put_args.add_argument('place', type = str)
theater_put_args.add_argument('location', type = str)
theater_put_args.add_argument('capacity', type = int)
theater_put_args.add_argument('rating', type = float)



class TheaterAPI(Resource):
    @marshal_with(resource_fields)
    def get(self, theater_id):
        theater = Theater.query.filter_by(theater_id=theater_id).first()
        if not theater:
            return abort(404,message="theater does\'t exist")
        return theater, 200
    

    def post(self):
        args = theater_post_args.parse_args()
        theater = Theater.query.filter_by(theater_id=args['theater_name']).first()
        if theater:
            return abort(409,message="theater already exist" )
        else:
            input = Theater(theater_name = args['theater_name'], place = args['place'], location =args['location'] , capacity  = args['capacity'], rating = args['rating'])
            db.session.add(input)
            db.session.commit()
            return jsonify({'status':'success', 'message':'data is added'})
        
    
    def delete(self,theater_id):
        theater = Theater.query.filter_by(theater_id=theater_id).first()
        if not theater:
            return abort(404,message="theater does\'t exist")
        db.session.delete(theater)
        db.session.commit()
        return jsonify({'status':'success', 'message':'theater deleted'})
    
    @marshal_with(resource_fields)
    def put(self, theater_id):
        args = theater_put_args.parse_args()
        theater = Theater.query.filter_by(theater_id=theater_id).first()
        if not theater:
            return abort(409,message="theater not exist" )
        if args['theater_name']:
            theater.theater_name = args['theater_name']
        if args['place']:
            theater.place = args['place']
        if args['location']:
            theater.location = args['location']
        if args['capacity']:
            theater.capacity = args['capacity']
        db.session.commit()
        return theater, 200


        

    


# {
#     "theater_name":"PVR",
#     "place": "delhi",
#     "location":"chandni chowk",
#     "capacity":20,
#     "rating":2.5
# }
