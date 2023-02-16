#!/usr/bin/env python3
"""
City class that inherit from BaseModel class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Defines public attributes"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiates instance of the class"""
        super().__init__(*args, **kwargs)
