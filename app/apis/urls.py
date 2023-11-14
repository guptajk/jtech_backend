from flask import Blueprint
from flask_restful import Api
from app.apis.resources.user import UserViews,user_routes

user_bp = Blueprint('user_api', __name__)
user_api = Api(user_bp)
user_api.add_resource(UserViews, *user_routes)