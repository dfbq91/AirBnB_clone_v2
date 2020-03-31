#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""

class DBStorage:
    """This class manage the data base"""
    __engine = None
    __session = None
    
    def __init__(self):
      """create the engine ant link to the MySQL database and
      user created before"""