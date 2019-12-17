#!/usr/bin/env python3.7
from user import User
from credentials import Credentials

def create_login(email,name,username,password)):
    """
    function to create a new account for password locker
    """
    new_user=User(email,name,username,password)
    return new_user

def save_login(user):
    """
    Function to save user login details
    """
    user.save_login()

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

def generate_password(length):
    """
    Function which generates a random password
    Args:
        the desired password length
    """
    return Credential.generate_password(length)

def main():
    print("hey there, welcome to password locker  ,we  can save your passwords safely for all your accounts and also generate new ones  but please first login ")

    while True:
        cprint(
            """
        Use the following short codes to manage your account 
            'lg' - Login 
            'xx' - Close app
            """)
        print("What would you like to do?")
        shortCode = input().lower()
         if shortCode == "lg":
            print("Do you have an account? Y or N")
            decision = input().lower()

            if decision.startswith("n"):
                email=input("enter your email")
                name=input("enter your name")
                username = input("Enter your username: ")
                password = input("Enter your password: ")#can use get pass method to show its a password is being entered
               
                print("\n")
                print("CONGRATULATIONS, YOUR ACCOUNT HAS BEEN CREATED")
                print("Sign into your new account")
                sign_in_name = input("Enter your username: ")
                sign_in_pin = input("Enter your pin: ")#get pass
                save_login(create_login(email,name,username,password))
                if authenticate_user(sign_in_name,sign_in_pin):
                    
                    print("SUCCESSFULLY SIGNED IN")  
                    print("\n")
                    pass
                else:
                    print("Oops, you entered the wrong username/pin, we have to do this again :(")
                    print("\n")
            else:
                sign_in_name = input("Enter your username: ")
                sign_in_pin = getpass("Enter your pin: ")
                if authenticate_user(sign_in_name,sign_in_pin):
                    
                    print("SUCCESSFULLY SIGNED IN")  
                    print("\n")
                    pass
                else:
                    print("Oops, you entered the wrong username/pin, we have to do this again :(")
                    print("\n")
