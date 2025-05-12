from . import db
from flask_login import UserMixin #contains tools for the login operation
from sqlalchemy.sql import func
class Note(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    data =db.Column(db.String(20000))
    date =db.Column(db.DateTime(timezone=True),default=func.now())
    user_id=db.Column(db.Integer,db.ForeignKey('user.id')) #lowercase to reference foreign key
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email= db.Column(db.String(100),unique=True)
    password=db.Column(db.String(150))
    firstName=db.Column(db.String(150))
    notes=db.relationship('Note') #uppercase in relationship defining