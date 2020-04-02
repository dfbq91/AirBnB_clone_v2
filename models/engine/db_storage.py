#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import environ
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

import sqlalchemy as db


class DBStorage:
    """This class manage the data base"""
    __engine = None
    __session = None

    def __init__(self):
        """create the engine ant link to the MySQL database and
        user created before"""

        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        hbn_env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)

        if hbn_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''query on the current database session all objects
        depending of the class name (argument cls)'''
        all_objs = {}
        all_classes = ["User", "State", "City", "Amenity", "Place", "Review"]
        if cls is None:
            for myclass in all_classes:
                objects = self.__session.query(eval(myclass))
            for obj in objects:
                key = "{}.{}".format(type(obj).__name__, obj.id).all()
                all_objs[key] = obj
        else:
            objects = self.__session.query(eval(cls)).all()
            for obj in objects:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                all_objs[key] = obj
        return all_objs

    def new(self, obj):
        '''add the object to the current database session (self.__session)'''
        if obj:
            self.__session.add(obj)

    def save(self):
        '''commit all changes of the current database
        session (self.__session)'''
        try:
            self.__session.commit()
        except InvalidRequestError:
            pass

    def delete(self, obj=None):
        '''delete from the current database session obj if not None'''
        if obj is not None:
            self.__session.delete(eval(obj))

    def reload(self):
        '''create all tables in the database'''
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()
