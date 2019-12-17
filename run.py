#!/usr/bin/env python3.7
from user import User
from credentials import Credentials

def create_login(email,name,username,password):
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
    return Credentials.credential_exist()

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

            while True:
                if authenticate_user(sign_in_name,sign_in_pin):
                    print(  """
                            welcome to password locker
                            use the following commands:
                            'cc' - enables you to create an a credential
                            'dc' - displays the credentials you have saved
                            'fc' - helps you find a credential by its social name
                            'dl' - deletes a credential
                            'ex' - logs you out
                            'help' - helps a user around the app
                            """
                            )
                    print(f"{sign_in_name}, what task would you like to perform?")
                    key_word = input().lower()

                    if key_word == 'cc':
                        print("Save a new credential")
                        social_app_name = input("Input social app name: ")
                        print("\n")
                        username = input("Input your username: ")
                        print("\n")
                        option = input("Would you wish to have Vault generate a password for you? Y or N ").lower()
                        if option.startswith("y"):
                            print()
                            desired_len = int(input("How long would you like your password to be? Provide number only. "))
                            password = generate_password(desired_len)
                        else:
                            print("\n")
                            password = input("Enter your password: ")

                        save_credentials(create_existing_credentials(social_app_name,username,password))
                        print('\n')
                        print(f"NEW CREDENTIALS FOR {social_app_name} CREATED!")
                        print("_"*50)
                        print('\n')

                    elif key_word == 'dc':

                        if display_credentials():
                            print("HERE ARE YOUR CREDENTIALS")
                            print('\n')

                            for cred in display_credentials():
                                print(
                                    f"""
    --------------------------------------------------
            Platform --- {credentials.social_app_name}               
            Username --- {credentials.app_username}                                
            Password --- {credentials.app_password}               
    --------------------------------------------------
                                """,
                                )
                                print('\n')
                        else:
                            print('\n')
                            print("You dont seem to have any credentials saved yet")
                            print("_"*50)
                            print('\n')

                    elif key_word == 'fc':
                        print("Enter the platform you want to search for")
                        print("\n")
                        platform_search = input()
                        if check_credential_exist(platform_search):
                            search_credential = find_credential(platform_search)
                            print(
                                f"""
    -------------------------------------------------------
        Platform --- {search_credential.social_app_name}               
        Username --- {search_credential.app_username}                               
        Password --- {search_credential.app_password}               
    -------------------------------------------------------
                                """)
                            print("_"*50)
                        else:
                            print("The credential does not exist")

                    elif key_word == "dl":
                        print("Enter the platform whose credentials you'd like to delete")
                        platform_delete = input()
                        if check_existing_credential(platform_delete):
                            platform_creds = find_credential(platform_delete)
                            delete_credential(platform_creds)
                            print(f"CREDENTIALS FOR {platform_creds.app_username} ")
                        else:
                            print("The credential does not exist") 

                    elif key_word == "ex":
                        print(f"Have a nice day {login_name}")
                        print("_"*50)
                        break
                
                else:
                    print("Oops, you entered the wrong username/pin, we have to do this again :(")
                    print("\n")
                    break

        elif shortCode == "xx":
            print("GOODBYE")
            break
        
        else:
            print("You entered an unknown short code, please try again")

if __name__ == '__main__':
    main()
                    

