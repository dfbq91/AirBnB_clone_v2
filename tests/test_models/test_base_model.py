#!/usr/bin/python3
"""test for BaseModel"""
import unittest
import os
from models.base_model import BaseModel
from models.base_model import State
from models.engine.file_storage import FileStorage
from datetime import datetime
import MySQLdb
import pep8


class TestBaseModel(unittest.TestCase):
    """this will test the base model class"""

    #def setUp(self):
        #'''Object created from a class'''
        #self.my_object = BaseModel()
        #self.db = MySQLdb.connect(host='localhost', user=hbnb_test,
                         #passwd=hbnb_test, db=hbnb_test_db)

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.base

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_BaseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """chekcing if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """test if the base is an type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save_BaesModel(self):
        """test if the save works"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """test if dictionary works"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    def test_executable_file(self):
        '''test if file has permissions u+x to execute'''
        # Check for read access
        is_read_true = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        '''check if my_object is an instance of BaseModel'''
        self.assertIsInstance(self.my_object, BaseModel)

    def test_id(self):
        '''test if the id of two instances are different'''
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_str(self):
        '''check if the output of str is in the specified format'''
        _dict = self.my_object.__dict__
        string1 = "[BaseModel] ({}) {}".format(self.my_object.id, _dict)
        string2 = str(self.my_object)
        self.assertEqual(string1, string2)

    def test_kwargs(self):
        '''check when a dictionary in sent as **kwargs argument'''
        self.my_object.name = "Holberton"
        self.my_object.my_number = 89
        my_object_json = self.my_object.to_dict()
        my_object_kwargs = BaseModel(**my_object_json)
        self.assertNotEqual(my_object_kwargs, self.my_object)

    def test_des_and_serialization(self):
        '''check serialization and deserialization'''
        storage = FileStorage()
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict, "es diccionario")  # Test all
        self.my_object.name = "Paparoachchchch"
        self.my_object.my_number = 95
        self.my_object.save()
        with open("file.json", "r", encoding='utf-8') as f:
            self.assertTrue(self.my_object.name in f.read())  # Test save

    def test_delete(self):
        '''check if a instance of the storage is deleted'''
        
if __name__ == "__main__":
    unittest.main()
