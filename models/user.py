#!/usr/bin/env python3
"""
User class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines public attributes."""

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """Initialize the public attributes"""
        super().__init__(*args, **kwargs)
