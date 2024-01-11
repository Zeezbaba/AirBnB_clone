#!/usr/bin/python3
"""File storage Class"""
import os
import datetime
import json


class FileStorage:

    """data storage and retrieval class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as files:
            dic = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(dic, files)

    def classes(self):
        """manage correctly serialization and deserialization of all our new classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}
        return classes

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as files:
            obj_dict = json.load(files)
            obj_dict = {key: self.classes()[obj["__class__"]](**obj)
                    for key, obj in obj_dict.items()}
            # Initialize FileStorage and calls for reload
            FileStorage.__objects = obj_dict

    def attributes(self):
        """returns attributes and types"""
        attributes = {
                "BaseModel":
                    {"id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime},
                "User":
                    {"email": str,
                        "password": str,
                        "first_name": str,
                        "last_name": str},
                "State":
                    {"name": str},
                "City":
                    {"state_id": str,
                    "name": str},
                "Amenity":
                    {"name": str},
                "Place":
                    {"city_id": str,
                    "user_id": str,
                    "name": str,
                    "description": str,
                    "number_rooms": int,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "price_by_night": int,
                    "latitude": float,
                    "longitude": float,
                    "amenity_ids": list},
                "Review":
                    {"place_id": str,
                        "user_id": str,
                        "text": str}
                    }
        return attributes
