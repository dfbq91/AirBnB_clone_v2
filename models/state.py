#!/usr/bin/python3
"""This is the state class"""
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            '''returns the list of City instances with
            state_id equals to the current State.id'''
            all_cities = models.storage.all(City)
            cities_in_state = []
            for key, value in all_cities.items():
                try:
                    if value.state_id == self.id:
                        cities_in_state.append(value)
                except BaseException:
                    pass
            return cities_in_state
