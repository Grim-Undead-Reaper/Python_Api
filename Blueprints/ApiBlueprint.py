from flask import Blueprint

apibp = Blueprint("apiBlueprint", __name__, url_prefix="/api")

@apibp.route("/users")
def Users():
    return ""

@apibp.route("/add/<username>")
def AddUser():
    return ""

@apibp.route("/delete/<username>")
def DeleteUser():
    return ""

@apibp.route("/update/<oldusername>/<newusername>")
def UpdateUser():
    return ""