#!/usr/bin/python3
'''This module defines all basics classes for the project'''
import uuid
import datetime


class BaseModel:
    '''BaseModel defines all common attributes/methods for other classes
    '''
    def __init__(self, *args, **kwargs):
        '''Initialization
        Args:
            args (list):
            kwargs (dict):
        '''
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

    def save(self):
        '''updates the public instance attribute updated_at
        with the current datetime
        '''
        self.updated_at = datetime.datetime.now()
        storage.save()
    
    def to_dict(self):
        '''function that returns a dictionary containing all keys/values
        of __dict__ of the instance
        '''
        ins_dict = self.__dict__.copy()
        ins_dict['__class__'] = type(self).__name__
        ins_dict['created_at'] = ins_dict['created_at'].isoformat()
        ins_dict['updated_at'] = ins_dict['updated_at'].isoformat()
        return (ins_dict)

    def __str__(self):
        '''String representation of an instance'''
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))
