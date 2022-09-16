import sys
import time
import unittest

sys.path.append("../")
from Tests.BaseTest import BaseTest



class Login(BaseTest):

    def setUp(self):
        super().setUp()
        self.email = self.generate_random_email()

    def test001_hp_login_correctly(self):
        """
            TC001: Verify that the login is working correctly
            1- Go to the website --> Sign-in
            2- Register for a new user --> Fill the registration form
            3- Login using the {} email and correct password
        """.format(self.email)

        self.LOGGER.info("Clicking on sign-in button")
        self.home_page.click_signin_btn()

        self.LOGGER.info("Opening the registration page")
        self.login_page.go_to_register_page(self.email)

        self.LOGGER.info("Filling the registration form")
        self.register_page.register("ahmed", "ramzy", 'Ahmed1234$')

        self.LOGGER.info("Signout")
        self.myacc_page.signout()

        self.LOGGER.info("Logging with the credentials")
        self.login_page.login_using_username_password(self.email, "Ahmed1234$")

        # Make sure that  you logged in correctly
        self.assertEqual(self.myacc_page.get_website_title(), "My account - My Store")

    def test002_login_with_unregistered_email(self):
        """
            TC002: Verify that the login will show an error when passing wrong username
            1- Go to the website --> Sign-in
            2- Login using wrong email 
        """

        self.LOGGER.info("Clicking on sign-in button")
        self.home_page.click_signin_btn()

        self.LOGGER.info("Logging with unregistered email and password")
        self.login_page.login_using_username_password(self.email, "Ahmed1234$")

        # Make sure that  you logged in correctly
        self.assertEqual("Authentication failed.",self.login_page.get_error())

    def test003_login_with_wrong_password(self):
        """
            TC003: Verify that the login is working correctly
            1- Go to the website --> Sign-in
            2- Register for a new user --> Fill the registration form
            3- Login using the {} email and wrong password"
        """.format(self.email)

        self.LOGGER.info("Clicking on sign-in button")
        self.home_page.click_signin_btn()

        self.LOGGER.info("Opening the registration page")
        self.login_page.go_to_register_page(self.email)

        self.LOGGER.info("Filling the registration form")
        self.register_page.register("ahmed", "ramzy", 'Ahmed1234$')

        self.LOGGER.info("Signout")
        self.myacc_page.signout()

        self.LOGGER.info("Logging with the email and wrong password")
        self.login_page.login_using_username_password(self.email, "12345")

        # Make sure that  you logged in correctly
        self.assertEqual("Authentication failed.",self.login_page.get_error())


