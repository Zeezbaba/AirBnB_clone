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
