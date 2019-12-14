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

if __name__ == '__main__':
    unittest.main()