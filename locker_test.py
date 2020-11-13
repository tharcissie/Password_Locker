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

    def test_init(self):
        """
        est to check if a new Credentials has been created correctly
        """
        self.assertEqual(self.credential.account_name,'Twitter')
        self.assertEqual(self.credential.user_name,'tharcissie')
        self.assertEqual(self.credential.account_password,'idufashe')   

    def save_credential_test(self):
        """
         test if the credential  is saved .
        """
        self.credential.save_credential()
        self.assertEqual(len(Credential.credentials),1) 


    def tearDown(self):
        '''
        method that clean after each test runned.
        '''
        Credential.credentials = []

    def test_save_multiple_accounts(self):
        '''
        test to check if we can save multiple credentials 
        '''
        self.credential.save_credential()
        test_credential = Credential("Istagram","Benitha","dudu") 
        test_credential.save_credential()
        self.assertEqual(len(Credential.credentials),2)

    def test_deleted_credential(self):
        """
        test if we can delete account credential
        """
        self.credential.save_credential()
        test_credential = Credential("Istagram","Benitha","dudu") 
        test_credential.save_credential()
        self.credential.delete_credential()
        self.assertEqual(len(Credential.credentials),1)   

if __name__ == '__main__':
    unittest.main()
        


