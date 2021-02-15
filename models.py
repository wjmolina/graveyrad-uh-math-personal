from flask_login import UserMixin
from sqlalchemy.orm import backref

from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


user_problem = db.Table('user_problem',
                        db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                        db.Column('problem_id', db.Integer, db.ForeignKey('problem.id'), primary_key=True)
                        )


class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
    users = db.relationship(
        'User',
        secondary=user_problem,
        backref=db.backref('problems')
    )
    difficulty = db.Column(db.Integer, nullable=False)
