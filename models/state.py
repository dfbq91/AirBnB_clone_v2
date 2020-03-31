#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    @property
    def cities(self):
        '''returns the list of City instances with
        state_id equals to the current State.id'''
        all_cities = models.storage.all(City)
        cities_in_state = []
        for city in all_cities.values():
            if city.state_id == self.id:
                cityes_in_state.append(city)
        return cities_in_
