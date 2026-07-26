from flask import Blueprint, render_template
from Constants import ListOfRoutes

allroutesbp = Blueprint("AllRoutesBlueprint", __name__, url_prefix="/routes")

@allroutesbp.route("")
def AllRoutesFrontend():
    return render_template("AllRoutes.html", routes=ListOfRoutes)