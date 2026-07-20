from flask import Blueprint, render_template

authbp = Blueprint("AuthenticationBlueprint", __name__, url_prefix="/auth")

@authbp.route("/register", methods=["POST", "GET"])
def register():
    return render_template("AuthenticationPage.html")

@authbp.route("/login", methods=["POST", "GET"])
def login():
    return render_template("AuthenticationPage.html")