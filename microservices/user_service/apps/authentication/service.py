from apps.authentication.dao import authentication_dao
from utils.response import Response


class AuthenticationService:
    def create_user(self, first_name, last_name, email, password):
        return authentication_dao.create_user(first_name, last_name, email, password)

    def validate_user(self, email, password):
        response = authentication_dao.get_user_by_email(email=email)

        if response.is_success:  # Email Id found in DB
            if password == response.result.password:
                return Response()
            else:
                return Response(is_success=False, message="Invalid Password")
        else:
            return Response(is_success=False, message="Invalid Username")
