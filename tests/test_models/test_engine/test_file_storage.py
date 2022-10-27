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
        self.asserTrue(fs)

    def test_verify_class_attributes(self):
        ''''''
        fs = FileStorage()
        assertTrue(hasattr(fs, 'objects'))
        assertTrue(hasattr(fs, 'file_path'))
    
    def test_verify_class_attributes_type(self):
        ''''''
        fs = FileStorage()
        obj = FileStorage.all()
        assertEqual(type(fs.objects), 'FileStorage')

    def test_verify_class_methods_all(self):
        ''''''
        fs = FileStorage()



if __name__ == '__main__':
    unittest.main()
