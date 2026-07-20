from extensions import db
from sqlalchemy import Column, Text, Integer, VARCHAR, ForeignKey
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(Text, nullable=False, unique=True)
    password = Column(VARCHAR(16), nullable=False, unique=False)

class Message(db.Model):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = db.relationship("User", backref=db.backref("user", uselist=False))
    message_text = Column(VARCHAR(200), unique=False, )