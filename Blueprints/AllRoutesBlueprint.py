from flask import Blueprint, render_template
from Constantes import AllRoutes

allroutesbp = Blueprint("AllRoutesBlueprint", __name__, url_prefix="/routes")

@allroutesbp.routes("")
def AllRoutesFrontend():
    return render_template("AllRoutes.html", routes=AllRoutes)