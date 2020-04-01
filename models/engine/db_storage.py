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
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from os import environ

class DBStorage:
    """This class manage the data base"""
    __engine = None
    __session = None
    
    def __init__(self):
      """create the engine ant link to the MySQL database and
      user created before"""
      
      
      user = environ['HBNB_MYSQL_USER']
      password = environ['HBNB_MYSQL_PWD']
      host = environ['HBNB_MYSQL_HOST']
      database = environ['HBNB_MYSQL_DB']
      hbn_env = environ['HBNB_ENV']
         
      self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(user, password, host, database), pool_pre_ping=True)
      Session = sessionmaker(bind = engine)
      
      if hbn_env == 'test':
          