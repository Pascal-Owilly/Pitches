import unittest
from pitch.models import User,Pitch
from . import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username='pascal',email='pascalouma54@gmail.com',password = 'abc123')
        
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
        
    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('abc123'))
        

if __name__=='__main__':
    unittest.main()