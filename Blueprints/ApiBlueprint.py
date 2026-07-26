from flask import Blueprint, json

apibp = Blueprint("apiBlueprint", __name__, url_prefix="/api")

@apibp.route("/users")
def Users():
    return ""

@apibp.route("/add/<name>")
def AddUser(name):
    return f"usuario {name} adicionado com sucesso"

@apibp.route("/delete/<name>")
def DeleteUser(name):
    return f"usuario {name} deletado com sucesso"

@apibp.route("/update/<oldname>/<newname>")
def UpdateUser(oldname, newname):
    return f"{oldname} foi substituido por {newname}"

@apibp.route("/routes")
def GetAllRoutes():
    with open('AllRoutes.json', 'r') as file:
        json_data = json.load(file)

    return json_data