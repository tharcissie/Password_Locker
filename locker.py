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

    @classmethod
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
    Credentials = []

    def __init__(self, account_name,user_name, account_password):
        '''
        new instance of class credential
        '''

    @classmethod
    def user(cls,username,password):
        '''
        function to help us to know if a user exit
        '''
         for user in User.users:
            if(user.username == username and user.password == password):
                user == user.username
            return user





