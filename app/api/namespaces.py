from flask_restx import Namespace

users_ns = Namespace('Users', path='/users', description='Users APIs')
posts_ns = Namespace('Posts', path='/posts', description='Posts APIs')
