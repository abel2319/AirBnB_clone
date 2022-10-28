#!/usr/bin/python3
''''''
import unittest
from datetime import datetime
import uuid

from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''Test class for BaseModel class
    '''
    def test_verify_instance(self):
        ''''''
        fs = FileStorage()
        self.assertTrue(fs)

    def test_verify_class_attributes(self):
        ''''''
        fs = FileStorage()
        self.assertFalse(hasattr(fs, '__objects'))
        self.assertFalse(hasattr(fs, '__file_path'))
    
    def test_verify_class_attributes_type(self):
        ''''''
        fs = FileStorage()
        obj = fs.all()
        #self.assertEqual(type(fs.objects), dict)

    def test_verify_class_methods_all(self):
        ''''''
        fs = FileStorage()
        dict1 = fs.all()
        self.assertEqual(type(dict1).__name__, 'dict')



if __name__ == '__main__':
    unittest.main()
