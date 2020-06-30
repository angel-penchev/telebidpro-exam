# Imports
from flask import Response, Blueprint, render_template, request
from server.database.database import calculate_new_request

# Config
routes_blueprint = Blueprint("routes", __name__)


# Routes
@routes_blueprint.route("/", methods=["GET", "POST"])
def index_route():
    result = 0
    if request.method == 'POST':
        A = request.form["A"]
        B = request.form["B"]
        name = request.form["name"]

        if not A or not B:
            return render_template('index.html', error="Input cannot be an empty string!")

        A = float(A)
        B = float(B)

        if B == 0:
            return render_template('index.html', error="Cannot devide by 0!")

        result = calculate_new_request(A, B, name)

    return render_template("index.html", result=result)
