#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
from db import DB
from user import User  # make sure this is correctly imported from your models


def _hash_password(password: str) -> bytes:
    """
    Hash a password with bcrypt and return salted hash as bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.
        - If user with email already exists, raise ValueError
        - Else, hash the password, create and return the new User
        """
        try:
            # Check if the user already exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except Exception:
            # User not found, safe to create
            hashed_pwd = _hash_password(password)
            new_user = self._db.add_user(email, hashed_pwd)
            return new_user
