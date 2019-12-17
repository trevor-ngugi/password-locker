#!/usr/bin/env python3.7
from user import User
from credentials import Credentials

def create_login(email,name,username,password)):
    """
    function to create a new account for password locker
    """
    new_user=User(email,name,username,password)
    return new_user

def create_existing_credentials(social_app_name ,app_username , app_password):
    """
    function to create existing credentials accounts 
    """
    new_credential=Credentials(social_app_name ,app_username , app_password)
    return new_credential

def save_credentials(credential):
    """
    function to save credentials
    """
    credential.save_credentials()

def delete_credential(credential):
    """
    function to delete credentials
    """
    credential.delete_credential()

def find_credential(appName):
    """
    function tofind credentials details
    """
    return Credentials.find_account(appName)

def check_credential_exist(username):
    """
    function to check if a credential exist
    """
    return.Credentials.credential_exist()

def display_credentials():
    """
    function that returns a list of credentials listed
    """
    return Credentials.credential_display()

def authenticate_user(username,password):
    return User.user_auth(username,password)

    