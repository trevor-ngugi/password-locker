import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    test class for users behaviours
    """
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user=User("ngugi@gmail.com","trevor","ngugstar","password123")

    def test_init(self):
        """
        test case to see if the objects are initialised corectly
        """
        self.assertEqual(self.new_user.email,"ngugi@gmail.com")
        self.assertEqual(self.new_user.name,"trevor")
        self.assertEqual(self.new_user.username,"ngugstar")
        self.assertEqual(self.new_user.password,"password123")

    def test_save_login(self):
        """
        test case to check if the objects are saved in the user list
        """
        self.new_user.save_login()
        self.assertEqual(len(User.user_list,),1)

    def test_user_auth(self):
        """
        test_user_auth tests case to authenticate the user
        """
        self.new_user.save_login()
        test_user=User("t@gmail.com","trevor","t.ngugi","321password")
        test_user.save_login()
        self.assertTrue(self.new_user.user_auth("t.ngugi","321password"))
    

if __name__ == '__main__':
    unittest.main()