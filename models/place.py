#!/usr/bin/python3
"""This is the place class"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship


plc_amty = Table('place_amenity', Base.metadata,
                 Column('place_id', String(60),
                        ForeignKey('places.id'),
                        nullable=False,
                        primary_key=True),
                 Column('amenity_id', String(60),
                        ForeignKey('amenities.id'),
                        nullable=False,
                        primary_key=True))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary="place_amenity")

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            '''returns the list of Review instances with
            place_id equals to the current Place.id'''
            all_reviews = models.storage.all(Review)
            rvws = []
            for rev in all_reviews.values():
                if rev.id in self.id:
                    rvws.append(rev)
            return rvws

        @property
        def amenities(self):
            '''get the list of amenities'''
            amnt = []
            all_amenities = models.storage.all(Amenity)
            for ame in all_amenities.values():
                if ame.id in self.amenity_ids:
                    amnt.append(ame)
            return amnt

        @amenities.setter
        def amenities(self, obj):
            '''set ids of amenities'''
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
