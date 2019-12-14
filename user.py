class User:
    """
    class that geneerates new users and login information
    """
    user_list=[]

    def __init__(self,email,name,username,password):
        self.email=email
        self.name=name
        self.username=username
        self.password=password

