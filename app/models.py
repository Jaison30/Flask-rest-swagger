from flask import url_for
from datetime import datetime
from . import db


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def to_json(self):
        json_post = {
            'post id': self.id,
            'author id': self.author_id,
            'body': self.body,
            'timestamp': self.timestamp,
        }
        return json_post


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True)
    email = db.Column(db.String(80), unique=True, index=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def to_json(self):
        json_user = {
            'username': self.username,
            'email': self.email,
            'post_count': self.posts.count()
        }
        return json_user
