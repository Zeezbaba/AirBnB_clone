#!/usr/bin/python3
"""The user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Manages user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

