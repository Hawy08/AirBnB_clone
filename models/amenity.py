#!/usr/bin/python3
"""
Amenity class module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class - inherits from BaseModel

    Attributes:
        name(str): name of the amenity
    """
    name = ""
