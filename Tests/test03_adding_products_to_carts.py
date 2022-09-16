import sys
sys.path.append("../")

from Tests.BaseTest import BaseTest
import time

class AddToCart(BaseTest):

    def setUp(self):
        super().setUp()
        self.item_name = 'Blouse'
        self.email = self.generate_random_email()
        self.count = 1
        self.size = 'M'
        self.color = 'White'


    def test001_add_item_to_cart(self):
        """
            TC001: Verify that adding a the {} to the cart is working correctly
            1- Go to the website --> Sign-in
            2- Register for a new user --> Fill the registration form
            3- Login using the {} email and correct password
            4- Searching for the {} in the home page
            5- CLicking  on the item
            6- Add to the  cart
        """.format(self.item_name, self.email,self.item_name)

        self.LOGGER.info("Clicking on sign-in button")
        self.home_page.click_signin_btn()

        self.LOGGER.info("Opening the registration page")
        self.login_page.go_to_register_page(self.email)

        self.LOGGER.info("Filling the registration form")
        self.register_page.register("ahmed", "ramzy", 'Ahmed1234$')

        self.LOGGER.info("Signout")
        self.myacc_page.signout()

        self.LOGGER.info("Loging with the credentials")
        self.login_page.login_using_username_password(self.email, "Ahmed1234$")
        self.assertEqual(self.myacc_page.get_website_title(), "My account - My Store")

        self.LOGGER.info("Go back to the home page")
        self.myacc_page.go_to_homepage()

        self.LOGGER.info("Searching for a {} in the home page table and clicking  on it ".format(self.item_name))
        result = self.home_page.search_and_click_on_item(self.item_name)

        self.LOGGER.info("Adding the {} to the cart ".format(self.item_name))
        self.product_page.Add_to_cart(self.count,self.size,self.color)

        self.assertEqual(self.checkout_page.get_website_title(),'Order - My Store')




