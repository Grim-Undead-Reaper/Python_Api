from __init__ import app

@app.route("/")
def home():
    return "Hello world"

@app.route("/add/<name>", methods=["POST"])
def AddNewUser(name:str):
    return f"Name: {name}"

@app.route("/update/<oldname>/<newname>", methods=["POST"])
def UpdateUser(oldname:str, newname:str):
    return f"Oldname: {oldname}\nNewname: {newname}"

@app.route("/delete/<name>", methods=["POST"])
def DeleteUser(name:str):
    return f"Name: {name}"

@app.route("/search/<name>", methods=["POST", "GET"])
def SearchUser(name:str):
    return f"Name: {name}"