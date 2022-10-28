#!/usr/bin/python3
''''''



class FileStorage:
    ''''''
    __file_path = ''
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
        json.dump(my_obj, file)
    
    def reload(self):
        '''Reload all objects from a json file
        '''
        with open(self.__file_path, encoding="utf-8") as file:
        return (json.load(file))
