from flask import jsonify, current_app, request
from flask_restx import Resource
from .. import users_ns

from ...models import Post, User


@users_ns.route("/<int:id>")
class GetUser(Resource):
    def get(self, id):
        user = User.query.get_or_404(id)
        return jsonify(user.to_json())


@users_ns.route("/<int:id>/posts/")
class GetUserPosts(Resource):
    def get(self, id):
        user = User.query.get_or_404(id)
        page = request.args.get('page', 1, type=int)
        pagination = user.posts.order_by(Post.timestamp.desc()).paginate(
            page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
            error_out=False)
        posts = pagination.items
        return jsonify({
            'posts': [post.to_json() for post in posts],
            'count': pagination.total
        })
