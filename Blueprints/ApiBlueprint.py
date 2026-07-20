from flask import Blueprint
from Constantes import AllRoutes

apibp = Blueprint("apiBlueprint", __name__, url_prefix="/api")

@apibp.route("/users")
def Users():
    return ""

@apibp.route("/add/<name>")
def AddUser():
    return ""

@apibp.route("/delete/<name>")
def DeleteUser():
    return ""

@apibp.route("/update/<oldname>/<newname>")
def UpdateUser():
    return ""

@apibp.route("/routes")
def GetAllRoutes():
    return AllRoutes