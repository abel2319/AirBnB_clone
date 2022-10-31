#!/usr/bin/python3
'''This module contains the unit tests for the BaseModel class
'''
import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''Test class for BaseModel class
    '''
    '''---------------------------------------------------------------'''
    def test_if_BaseModel_is_instanciable(self):
        '''Instanciate BaseModel and verify the type of the instance
        '''
        base = BaseModel()
        self.assertEqual(type(base).__name__, 'BaseModel')

    def test_id_of_instance_of_BaseModel(self):
        '''Verify if id exist'''
        base = BaseModel()
        self.assertTrue(hasattr(base, 'id'))

    def test_verify_if_id_is_str(self):
        '''Verify if id is an str'''
        base = BaseModel()
        self.assertEqual(type(base.id), 'str')

    def test_verify_if_id_is_str(self):
        '''Verify if id is an uuid4'''
        base = BaseModel()
        self.assertEqual(uuid.UUID(base.id).version, 4)

    def test_createdat_of_instance_of_BaseModel(self):
        '''Verify if created_at attribute exist and
        if it is in datetime format'''
        base = BaseModel()
        self.assertTrue(hasattr(base, 'created_at'))
        self.assertTrue(type(base.created_at) is datetime)

    def test_updatedat_of_instance_of_BaseModel(self):
        '''Verify if created_at attribute exist and
        if it is in datetime format
        '''
        base = BaseModel()
        self.assertTrue(hasattr(base, 'updated_at'))
        self.assertTrue(type(base.updated_at) is datetime)

    def test_verif_if_created_and_updated_are_same(self):
        '''verify if created_at and updated_at are same when
        an object is created
        '''
        base = BaseModel()
        self.assertEqual(base.created_at, base.updated_at)

    def test_save_method(self):
        '''Verify if when the save() method is call the
        update_at attribute is update
        '''
        base = BaseModel()
        base.save()
        self.assertGreater(base.updated_at, base.created_at)

    def test_to_dict_method(self):
        '''Verify if when the save() method is call the
        update_at attribute is update
        '''
        base = BaseModel()
        dict1 = base.to_dict()
        self.assertTrue(hasattr(base, 'to_dict'))
        self.assertTrue(dict1)
        self.assertTrue('__class__' in dict1.keys())
#       self.assertEqual(type(dict1['created_at']), dict.isoformat())

    def test_str_method(self):
        '''Test represention of an instance'''
        base = BaseModel()
        rep = base.__str__()
        self.assertEqual("[{}] ({}) {}".format(type(base).__name__,
                                               base.id, base.__dict__), rep)
    '''-------------------------------------------------------------------'''

    def test_create_object_without_arguments(self):
        ''''''
        base = BaseModel()
        self.assertTrue(base)

    def test_create_object_with_args(self):
        ''''''
        base = BaseModel('airbnb', 404)
        self.assertTrue(base)

    def test_create_object_with_kwargs(self):
        ''''''
        base1 = BaseModel()
        kwargs = base1.to_dict()
        base2 = BaseModel(**kwargs)
        self.assertTrue(base2)

    def test_add_new_attribute_using_kwargs(self):
        ''''''
        base1 = BaseModel()
        kwargs = base1.to_dict()
        kwargs['name'] = 'airbnb'
        base2 = BaseModel(**kwargs)
        self.assertTrue(hasattr(base2, 'name'))


if __name__ == '__main__':
    unittest.main()
