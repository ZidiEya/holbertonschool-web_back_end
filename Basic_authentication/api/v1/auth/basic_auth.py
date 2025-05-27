#!/usr/bin/env python3
""" Basic Authentication """
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
import base64

User = TypeVar('User')


class BasicAuth(Auth):
    """ BasicAuth class inherits from Auth """

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> User:
        """
        Returns the User instance based on email and password
        """
        # Check if email and password are valid strings
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None

        # Try to find user by email
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        # No user found
        if not users or len(users) == 0:
            return None

        user = users[0]

        # Check password validity
        if not user.is_valid_password(user_pwd):
            return None

        return user
