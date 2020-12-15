from flask_login import UserMixin
from datetime import datetime
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    last_logged_in= db.Column(db.DateTime, default=datetime.utcnow())
    gifts = db.Column(db.String(100))
        