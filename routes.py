from __init__ import app, login_manager, db
from model import Usuario
from flask import render_template

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Usuario, user_id)

@app.route("/")
def home():
    return "Hello world"

@app.route("/add/<name>", methods=["POST"])
def AddNewUser(name:str):
    return f"Name: {name}"

@app.route("/register", methods=["POST", "GET"])
def register():
    return render_template("AuthenticationPage.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("AuthenticationPage.html")

@app.route("/update/<oldname>/<newname>", methods=["POST"])
def UpdateUser(oldname:str, newname:str):
    return f"Oldname: {oldname}\nNewname: {newname}"

@app.route("/delete/<name>", methods=["POST"])
def DeleteUser(name:str):
    return f"Name: {name}"

@app.route("/search/<name>", methods=["POST", "GET"])
def SearchUser(name:str):
    return f"Name: {name}"