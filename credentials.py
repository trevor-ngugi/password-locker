class Credentials:
    """
    class that generates  social app name,username,and password properties
    """
    credentials_list=[]

    def __init__(self,social_app_name ,app_username , app_password):
        self.social_app_name=social_app_name
        self.app_username=app_username
        self.app_password=app_password
        

    def save_credentials(self):
        """
        method to save the credentials object
        """
        Credentials.credentials_list.append(self)

    def delete_credential(self):
        """
        method to delete credentials
        """
        Credentials.credentials_list.remove(self)
        
    # @classmethod
    # def find_account(cls,appName,appUsername):
    #     """
    #     method that takes in app name and username and returns app name and username if matched
        
    #     args:
    #         app_name:takes in the app name to search name
    #         app_username:takes in the username of to sarch for

    #     returns:
    #         the account if the app username and app name if matched
    #     """
    #     for account in cls.credentials_list:
    #         if account.social_app_name and account.app_username==appName and appUsername:
    #             return account

    @classmethod
    def find_account(cls,appName):
        """
        method that takes in app name  and returns app name if matched
        
        args:
            app_name:takes in the app name to search name
            

        returns:
            the account if the app username if matched
        """
        for account in cls.credentials_list:
            if account.social_app_name == appName :
                return account

    @classmethod
    def credential_exist(cls,username):
        """
        method that takes in user name exist from the contact lsit
        args:
            username:takes in the username to search if it exist
        returns:
            bolean :returns the credentials if exists
        """
        for account in cls.credentials_list:
            if account.app_username == username :
                return True
        return False

