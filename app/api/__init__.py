
# from . import posts
#from . import posts
from flask import Blueprint
from flask_restx import Api

from .namespaces import users_ns
from .namespaces import posts_ns
from . import endpoints

__endpoints__ = endpoints


api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint, title='Blog Posts',
          description='Blog Posts swagger')
api.add_namespace(users_ns)
api.add_namespace(posts_ns)
