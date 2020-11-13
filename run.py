#!/usr/bin/env python3.6
from locker import User, Credential

def create_user(username, password):
    '''
    function to create a user
    '''
    user = User(username,password)
    return user

def save_user(user):
    '''
    function to save a user
    '''
    user.save_user()

def list_users():
    '''
    function to display all users
    '''
    return User.list_users()

def user_checker(username,password):
    '''
    to check if user exist
    '''
    user_checker = Credential.user_checker(username,password)
    return user_checker

def create_credential(username,password,account_name):
    '''
    creating new account credential
    '''
    credential = Credential(username,password,account_name)
    return credential

def save_credential(credential):
    '''
    saving account credential
    '''
    credential.save_credential()

def delete_credential(credential):
    '''
    deleting an account credential
    '''
    credential.delete_credential()

def search_credential(credential):
    '''
    searching a certain account credential
    '''
    return Credential.search_credential(credential)

def view_all_credential():
    '''
    viewing all accounts credentials
    '''
    return Credential.view_all_credential()

def generate_password():
    '''
    generating a random password for a use
    '''
    password = Credential.generate_password()
    return password

def creadential_checker(credential):
    '''
    to check if credentials are true
    '''
    return Credential.creadential_checker(credential)

def main():
    print("Welcome to PASSWORD LOCKER...\n Enter the following abbreviation to continue:\n c ---------- Create an account \n l ---------- Login if you already have an account \n")
    abbreviation = input().lower()
    if abbreviation == 'c':
        print("Create an account in PASSWORD LOCKER")
        print("@"*20)
        username = input('User name: ')
        while True:
            print('Enter the following to continue: \n p ---------- Type a password\n g ---------- generate a password fro you\n')
            abbreviation = input().lower()
            if abbreviation == 'p':
                password = input("Enter a password for your account\n")
                break
            elif abbreviation == 'g':
                password = generate_password()
                break
            else:
                print('Invalid password')
            
        save(create_user(username,password))

    




    



