from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    link = db.Column(db.String(80), unique=True)

    def __init__(self, name=None, link=None):
        self.name = name
        self.link = link

    def __repr__(self):
        return '<id = {}, name = {}, link = {}>'.format(self.id, self.name, self.link)

