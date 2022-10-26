import imp
from flask import jsonify
from flask_restx import Resource

from .. import posts_ns
from ...models import Post


@posts_ns.route("")
class GetPosts(Resource):
    def get(self):
        posts = Post.query.all()
        return jsonify({'posts': [post.to_json() for post in posts]})


@posts_ns.route("/<int:id>")
class GetPostsById(Resource):
    def get(self, id):
        post = Post.query.get_or_404(id)
        return jsonify(post.to_json())



