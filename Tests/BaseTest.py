import sys
sys.path.append("../")

import unittest
from selenium import webdriver
from unittest import TestCase
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from Pages.WomenPage import WomenPage
from Pages.ProductPage import ProductPage
from Pages.CheckoutPage import CheckoutPage
from Pages.MyAccountPage import MyAccountsPage
from Pages.SearchResultPage import SearchResultPage
from Pages.AddressPage import AddressPage
from Pages.ShippingPage import ShippingPage
from Pages.PaymentPage import PaymentPage
from loguru import logger
import random
import HtmlTestRunner


class BaseTest(TestCase):

    LOGGER = logger
    LOGGER.add('logs/log_{time}.log', backtrace=False)

    def setUp(self):
        self.LOGGER.info("Executing testcase {}".format(self._testMethodName))
        self.LOGGER.info("Opening the website")
        self.driver = webdriver.Chrome(executable_path='/home/ahmed/Desktop/chromedriver')
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.multiformis.com/index.php')
        self.LOGGER.info("Website opened")

        # Loading the website pages
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.myacc_page = MyAccountsPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.register_page = RegisterPage(self.driver)
        self.searchresult_page = SearchResultPage(self.driver)
        self.women_page = WomenPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.address_page = AddressPage(self.driver)
        self.shipping_page = ShippingPage(self.driver)
        self.payment_page = PaymentPage(self.driver)

    def tearDown(self):
        self.LOGGER.info("Closing the website")
        self.driver.close()
        self.driver.quit()


    def generate_random_email(self):
        # Generate a random email for registration
        number = random.randint(10000, 99999)
        email = "Ahmed" + str(number) + "@gmail.com"
        return email


if __name__ == '__main__':
    testsuite = unittest.TestLoader().discover('.')
    HtmlTestRunner.HTMLTestRunner(combine_reports=True).run(testsuite)



