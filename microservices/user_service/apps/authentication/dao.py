from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.authentication.models import User
from utils.response import Response


class AuthenticationDao:
    @staticmethod
    def create_user(first_name, last_name, email, password):
        user = User(first_name, last_name, email, password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_email(
        email: str,
    ) -> tuple:
        result = None

        with db.session.begin():
            try:
                result = User.query.filter_by(email=email).first()

            except SQLAlchemyError as err:
                print(f"Failed to search user by email in database. {str(err)}.")
                return False, "Failed to update database.", None

        return Response(result=result)


authentication_dao = AuthenticationDao()
