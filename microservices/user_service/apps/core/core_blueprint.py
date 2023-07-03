from flask.blueprints import Blueprint
from flask import render_template


core_blueprint = Blueprint(
    "core", __name__, template_folder="templates", url_prefix="/api/core"
)


@core_blueprint.route("/", methods=["GET"])
@core_blueprint.route("/home", methods=["GET"])
def home():
    return render_template("home.html")
