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
        