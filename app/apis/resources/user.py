from flask_restful import Resource, reqparse
from flask import jsonify
from app import db
from app.auth_middleware import token_required
from app.models import User


class UserViews(Resource):

    # Define the request parser for parsing POST data
    user_parser = reqparse.RequestParser()
    user_parser.add_argument('username', type=str, required=True, help='Username is required.')
    user_parser.add_argument('email', type=str, required=True, help='Email is required.')

    @token_required
    def post(self):
        url = reqparse.request.url
        if "login" in url:
            self.login()
        else:
            args = self.user_parser.parse_args()
            username = args['username']
            email = args['email']
            user = User(username=username, email=email)
            db.session.add(user)
            db.session.commit()
            return {'message': 'User created successfully.'}

    @token_required
    def get(self):
        url = reqparse.request.url
        if "login" in url:
            self.login()
        else:
            users = User.query.all()
            user_list = []
            for user in users:
                user_list.append({'username': user.username, 'email': user.email})
            # return jsonify(user_list), 200
            return []


    def login(self):
        print("\n\t Login route....")

    def register(self):
        print("\n\t Register route....")


user_routes = ["/", "/login"]

