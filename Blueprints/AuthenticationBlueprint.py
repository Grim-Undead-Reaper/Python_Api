from flask import Blueprint, render_template

authbp = Blueprint("AuthenticationBlueprint", __name__, url_prefix="/auth")

@authbp.route("", methods=["POST", "GET"])
def Auth():
    return render_template("AuthenticationPage.html")