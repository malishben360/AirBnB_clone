#!/usr/bin/env python3
"""
State class that inherit from BaseModel class.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """Defines public attributes"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Use to initialize instances of the class"""
        super().__init__(*args, **kwargs)
