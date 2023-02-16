#!/usr/bin/env python3
"""
Review class that inherit from BaseModel class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines public attributes"""

    place_id = str("")
    user_id = str("")
    text = str("")

    def __init__(self, *args, **kwargs):
        """Instantiates instance of the class"""
        super().__init__(*args, **kwargs)
