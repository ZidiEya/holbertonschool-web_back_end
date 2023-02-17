#!/usr/bin/env python3
""" Create user, Find user, Update user """
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar
from user import Base, User


class DB:
    """ class """
    def __init__(self):
        """ constructor """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ create a session """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ save the user to the database and returns a User object """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ The method takes in arbitrary keyword arguments and
        returns the first row found in the users table as
        filtered by the method’s input arguments. No validation
        of input arguments required at this point. """
        if not kwargs:
            raise InvalidRequestError
        users_columns = [
            'id',
            'email',
            'hashed_password',
            'session_id',
            'reset_token'
        ]
        for arg in kwargs:
            if arg not in users_columns:
                raise InvalidRequestError

        """ search table for user """
        search_user = self.__session.query(User).filter_by(**kwargs).first()

        if search_user:
            return search_user
        else:
            raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """ finds user record and updates attributes """

        user_to_update = self.find_user_by(id=user_id)

        users_columns = [
            'id',
            'email',
            'hashed_password',
            'session_id',
            'reset_token'
            ]

        for k, v in kwargs.items():
            if k in users_columns:
                setattr(user_to_update, k, v)
            else:
                raise ValueError

        self._session.commit()
