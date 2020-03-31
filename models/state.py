#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel


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
      
