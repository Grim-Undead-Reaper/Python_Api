from flask import Flask
from dotenv import load_dotenv
from Blueprints.ApiBlueprint import apibp
from Blueprints.AuthenticationBlueprint import authbp
from extensions import db, lm
import os

load_dotenv(dotenv_path=r"Super_Secrets/MySecrets.env")

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///MeuDados.db"

lm.init_app(app)
db.init_app(app)

@lm.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

app.register_blueprint(apibp)
app.register_blueprint(authbp)
from model import *

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)