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

def save_credential



