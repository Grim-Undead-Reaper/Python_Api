from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_login import LoginManager
import os

load_dotenv(dotenv_path=r"Super_Secrets/MySecrets.env")

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///MeuDados.db"

login_manager = LoginManager(app)
db = SQLAlchemy(app)

from routes import *
from model import *

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)