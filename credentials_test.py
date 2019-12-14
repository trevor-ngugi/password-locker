import unittest
from credentials import Credentials

class  TestCredentials(unittest.TestCase):
    """
    test class for credentials behaviours
    """
    def setUp(self):
        """
        set up method to run befor each test
        """
        self.new_credentials=Credentials("instagram","t.ngugi","123password")

    def test_init(self):
        """
        to check if the objects are initialised correctly
        """
        self.assertEqual(self.new_credentials.social_app_name,"instagram")
        self.assertEqual(self.new_credentials.app_username,"t.ngugi")
        self.assertEqual(self.new_credentials.app_password,"123password")

if __name__=='__main__':
    unittest.main()