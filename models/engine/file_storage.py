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
        FileStorage.__objects
