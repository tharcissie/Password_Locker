import random

class User:
    '''
    create a user class
    '''

    users = []

    def __init__(self,username,password):
        '''
        generate new instance of a class user
        '''

        self.username = username
        self.password = password

    def save_user(self):
        '''
        function to save a user credentials
        '''
        User.users.append(self)

    @classmethod #This means you can use the class and its properties inside that method rather than a particular instance.
    def list_users(cls):
        '''
        method to display all credentials
        '''
        return cls.users

    def delete(cls):
        '''
        delete credential
        '''
        User.users.remove(self)

class Credential():
    '''
    class which helps us to create new creadential for a certain account
    '''  
    credentials = []

    def __init__(self, account_name,user_name, account_password):
        '''
        new instance of class credential
        '''
        self.account_name = account_name
        self.user_name = user_name
        self.account_password = account_password

    @classmethod
    def user_checker(cls,username,password):
        '''
        function to help us to know if a user exit
        '''
        for user in User.users:
            if(user.username == username and user.password == password):
                user == user.username
            return user

    def save_credential(self):
        '''
        method to save account credential
        '''
        Credential.credentials.append(self)

    def delete_credential(self):
        '''
        method to delete account crential
        '''
        Credential.credentials.remove(self)

    @classmethod
    def search_credential(cls,account_name):
        '''
        method to search for an count credential
        '''
        for credential in cls.credentials:
            if credential.account_name == account_name:
     
                return credential
    @classmethod
    def view_all_credential(cls):
        '''
        method to view all acount credential
        '''
        return cls.credentials

    def generate_password(self):
        self.account_password = random.randint(00000000,99999999)
        return self.user_nameaccount_password

    def creadential_checker(self):
        '''
        method to help us now if account exit
        '''
        for credential in credentials:
            if credential.account_name == account_name:
                return True
        return False









