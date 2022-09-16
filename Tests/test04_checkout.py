import sys
sys.path.append("../")
import time
from Tests.BaseTest import BaseTest


class CheckOut(BaseTest):

    def setUp(self):
        super().setUp()
        self.item_name = 'Blouse'
        self.email = self.generate_random_email()
        self.count = 1
        self.size = 'M'
        self.color = 'White'
        self.address = "Shobra st"
        self.city = "Cairo"
        self.state = "Alaska"
        self.zip_code = "12345"
        self.phone = "12345"
        self.address_alias = "New Address"

    def test001_validate_summary_step(self):
        """
            TC001: Validate that the prices are correct and proceed to the next step
            1- Go to the website --> Sign-in
            2- Register for a new user --> Fill the registration form
            3- Login using the {} email and correct password
            4- Searching for the {} in the home page
            5- CLicking  on the item
            6- Add to the  cart
            7- Validate on the prices then proceed
        """.format(self.item_name, self.email, self.item_name)

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
        self.product_page.Add_to_cart(self.count, self.size, self.color)

        self.LOGGER.info("Get the prices in the summary page")
        qty_count,unit_price,total_price,shipping_price,total_price_with_shipping=\
            self.checkout_page.return_prices()
        # Validate that the number of items are correct
        self.assertEqual(self.count,int(qty_count))
        # Validate that the total price is correct
        self.assertEqual(int(qty_count)*float(unit_price[1:]),float(total_price[1:]))
        # Validate that the total price after shipping is correct
        self.assertEqual(float(total_price[1:])+float(shipping_price[1:]),float(total_price_with_shipping[1:]))

        self.LOGGER.info("Proceed to next page")
        self.checkout_page.proceed_to_checkout()
        self.assertEqual(self.checkout_page.get_website_title(),'Address - My Store')

    def test002_validate_address_step(self):
        """
            TC002: Validate that the address step is working successfully
            1- Go to the website --> Sign-in
            2- Register for a n ew user --> Fill the registration form
            3- Login using the {} email and correct password
            4- Searching for the {} in the home page
            5- CLicking  on the item
            6- Add to the  cart and proceed
            7- Fill the address form
            8- Validate the address data is saved by checking address name
            9- Proceed
        """.format(self.item_name, self.email, self.item_name)

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
        self.product_page.Add_to_cart(self.count, self.size, self.color)

        self.LOGGER.info("Get the prices in the summary page")
        qty_count, unit_price, total_price, shipping_price, total_price_with_shipping = \
            self.checkout_page.return_prices()

        self.LOGGER.info("Proceed to next page")
        self.checkout_page.proceed_to_checkout()

        self.LOGGER.info("Fill the address form")
        self.address_page.fill_form(self.address,self.city,self.state,self.zip_code,self.phone,self.address_alias)
        self.assertEqual(self.address_page.get_address(),self.address)

        self.LOGGER.info("Proceed to next page")
        self.address_page.proceed_checkout()
        self.assertEqual(self.shipping_page.get_header_text(),'SHIPPING:')

    def test003_validate_shipping(self):
        """
            TC003: Validate that shipping step is working successfully
            1- Go to the website --> Sign-in
            2- Register for a n ew user --> Fill the registration form
            3- Login using the {} email and correct password
            4- Searching for the {} in the home page
            5- CLicking  on the item
            6- Add to the  cart and proceed
            7- Fill the address form and proceed
            8- Validate the shipping and  proceed
        """.format(self.item_name, self.email, self.item_name)

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
        self.product_page.Add_to_cart(self.count, self.size, self.color)

        self.LOGGER.info("Get the prices in the summary page")
        qty_count, unit_price, total_price, shipping_price, total_price_with_shipping = \
            self.checkout_page.return_prices()

        self.LOGGER.info("Proceed to next page")
        self.checkout_page.proceed_to_checkout()

        self.LOGGER.info("Fill the address form")
        self.address_page.fill_form(self.address,self.city,self.state,self.zip_code,self.phone,self.address_alias)

        self.LOGGER.info("Proceed to next page")
        self.address_page.proceed_checkout()

        self.LOGGER.info("Proceed to next page")
        self.shipping_page.proceed_to_checkout()
        self.assertEqual(self.payment_page.get_header_text()[:33],'PLEASE CHOOSE YOUR PAYMENT METHOD')


    def test004_validate_payment_method(self):
        """
            TC004: Validate that the payment step is working successfully
            1- Go to the website --> Sign-in
            2- Register for a n ew user --> Fill the registration form
            3- Login using the {} email and correct password
            4- Searching for the {} in the home page
            5- CLicking  on the item
            6- Add to the  cart and proceed
            7- Fill the address form and proceed
            8- Proceed the shipping
            9- Validate the payment prices and proceed
        """.format(self.item_name, self.email, self.item_name)

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
        self.product_page.Add_to_cart(self.count, self.size, self.color)

        self.LOGGER.info("Get the prices in the summary page")
        qty_count, unit_price, total_price, shipping_price, total_price_with_shipping = \
            self.checkout_page.return_prices()

        self.LOGGER.info("Proceed to next page")
        self.checkout_page.proceed_to_checkout()

        self.LOGGER.info("Fill the address form")
        self.address_page.fill_form(self.address,self.city,self.state,self.zip_code,self.phone,self.address_alias)

        self.LOGGER.info("Proceed to next page")
        self.address_page.proceed_checkout()

        self.LOGGER.info("Proceed to next page")
        self.shipping_page.proceed_to_checkout()

        self.LOGGER.info("Validate the final prices")
        final_qty,final_unit_price,final_shipping,final_total_ship_tax=\
            self.payment_page.get_final_prices()

        self.assertEqual(int(self.count), int(final_qty))
        self.assertEqual(float(unit_price[1:]), float(final_unit_price[1:]))
        self.assertEqual(float(final_shipping[1:]),float(shipping_price[1:]))
        self.assertEqual(float(total_price_with_shipping[1:]),float(final_total_ship_tax[1:]))

        self.LOGGER.info("Pay by bank wire")
        self.payment_page.pay_by_bank_wire()

        self.LOGGER.info("Confirm order the final prices")
        self.payment_page.confirm_order()
        self.assertEqual("Your order on My Store is complete.",self.payment_page.get_success_message())
