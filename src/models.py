from flask_login import UserMixin
from webapp import db

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    manager = db.Column(db.Boolean(), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


class Shift(db.Model):
    __tablename__ = "shifts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    time = db.Column(db.Integer)

    def __repr__(self):
        return '<Shift %r>' % self.time