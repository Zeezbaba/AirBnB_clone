#!/usr/bin/python3
"""module for a review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """manages the review objects"""

    place_id = ""
    user_id = ""
    text = ""
