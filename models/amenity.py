#!/usr/bin/env python3
"""
Amenity class that inherit from BaseModel class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines public attributes"""

    city_id = str("")
    user_id = str("")
    name = str("")
    description = str("")
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Instantiates instance of the class"""
        super().__init__(*args, **kwargs)
