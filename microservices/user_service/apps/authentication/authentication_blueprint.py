from flask.blueprints import Blueprint
from flask import redirect, url_for, render_template
from apps.authentication.forms import UserRegistration, UserLogin
from apps.authentication.service import AuthenticationService


authentication_blueprint = Blueprint(
    "authentication",
    __name__,
    template_folder="templates",
    url_prefix="/api/authentication",
)


@authentication_blueprint.route("/post_register", methods=["GET"])
def post_register():
    return render_template("post_registration.html")


@authentication_blueprint.route("/post_login", methods=["GET"])
def post_login():
    return render_template("post_login.html")


@authentication_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = UserRegistration()

    if form.validate_on_submit():  # Post request
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data

        authentication_service = AuthenticationService()
        authentication_service.create_user(first_name, last_name, email, password)

        return redirect(url_for("authentication.post_register"))

    return render_template("register.html", form=form)


@authentication_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = UserLogin()

    if form.validate_on_submit():  # Post request
        email = form.email.data
        password = form.password.data

        authentication_service = AuthenticationService()
        response = authentication_service.validate_user(email=email, password=password)

        if not response.is_success:
            print("Login is unsuccessfull")

        return redirect(url_for("authentication.post_login"))

    return render_template("login.html", form=form)
