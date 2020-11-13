import unittest
from locker import User
from locker import Credential

class User_Test(unittest.TestCase):
    '''
    class to test an user class
    '''
    def setUp(self):
        '''
        function that runs before
        '''
        self.user = User('tharcissie','idufashe')

    def test_init(self):
        '''
        to check if user is correctly created
        '''
        self.assertEqual(self.user.username,'tharcissie')
        self.assertEqual(self.user.password,'idufashe')


    def test_save_user(self):
        '''
        to test if user is saved
        '''
        self.user.save_user()
        self.assertEqual(len(User.users),1)

class Credential_Test(unittest.TestCase):
    '''
    class to test a credential class
    '''
    def setUp(self):
        '''
        function that runs before
        '''
        self.credential = Credential('Twitter','tharcissie','idufashe')
        



        

if __name__ == '__main__':
    unittest.main()
        


