from __init__ import db
from sqlalchemy import Column, Text, Integer, VARCHAR

class Usuario (db.Model):
    __tablename__ = "Usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    nome = Column(Text, nullable=False, unique=True)
    password = Column(VARCHAR(16), nullable=False, unique=False)