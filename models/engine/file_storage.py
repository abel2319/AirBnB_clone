#!/usr/bin/python3
'''module to define class FileStorage'''
import json


class FileStorage:
    '''class FileStorage that serializes instances
    to a JSON file and deserializes JSON file to instances
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Return all objects saved
        '''
        return (self.__objects)

    def new(self, obj):
        '''save an objects by adding it in __objects
        Args:
            obj (new object):
        '''
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        '''Save all objects in a json file
        '''
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            tmp = {}
            for key in self.__objects:
                tmp[key] = self.__objects[key].to_dict()
            json.dump(tmp, file)
    
    def reload(self):
        '''Reload all objects from a json file
        '''
        try:
            with open(self.__file_path, 'r') as file:
                tmp = json.load(file)
                for key in tmp:
                    keys = key.split('.')
                    if keys[0] == 'BaseModel':
                        self.__objects[key] = BaseModel(**tmp[key])
                    elif keys[0] == 'User':
                        self.__objects[key] = User(**tmp[key])
        except:
            return
