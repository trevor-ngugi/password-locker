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

    def test_save_credentials(self):
        """
        test case to check if the objects are being saved in the credentials_list
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        """
        does clean up after each test case has been done 
        """
        Credentials.credentials_list=[]

    def test_save_multiple_credentials(self):
        """
        test case to check if more credentials can be saved
        """
        self.new_credentials.save_credentials()
        test_credential=Credentials("facebook","t.ngugi","321password")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        """
        test case to check if we can delet credentials
        """
        self.new_credentials.save_credentials()
        test_credential=Credentials("facebook","t.ngugi","321password")
        test_credential.save_credentials()

        test_credential.delete_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_social_by_app_name_and_username(self):
        """
        test to check if we can find app name and username and display their passwords
        """
        self.new_credentials.save_credentials()
        test_credential=Credentials("facebook","t.ngugi","321password")
        test_credential.save_credentials()
        test_credential2=Credentials("facebook","trevor.ngugi","322password")
        test_credential2.save_credentials()

        found_account=Credentials.find_account("facebook","t.ngugi")
        self.assertEqual(found_account.app_password,test_credential.app_password)

        

if __name__=='__main__':
    unittest.main()