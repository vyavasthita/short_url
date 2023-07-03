from flask.blueprints import Blueprint
from apps.shortner.service import ShortnerService


shortner_blueprint = Blueprint(
    "shortner", __name__, url_prefix="/api/shortner"
)


@shortner_blueprint.route("/short", methods=["GET"])
def post_register():
    shortner_service = ShortnerService()
    response = shortner_service.get_short_url(long_url="https://github.com/vyavasthita/short_url")

    return response.result, 200