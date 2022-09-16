from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

class CheckoutPage():

    def __init__(self, driver):
        self.driver = driver
        self.total_price_id='total_product'
        self.shipping_price_id =  'total_shipping'
        self.total_price_without_tax_id ='total_price_without_tax'
        self.proceed_to_checkout_class = 'standard-checkout'
        self.qty_class = 'cart_quantity_input'
        self.unit_price_class = 'price'

    def return_prices(self):
        self.driver.implicitly_wait(5)
        total_price = self.driver.find_element(by=By.ID, value=self.total_price_id).text
        shipping_price = self.driver.find_element(by=By.ID, value=self.shipping_price_id).text
        total_price_without_taxes = self.driver.find_element(by=By.ID, value=self.total_price_without_tax_id).text
        qty_count = self.driver.find_element(by=By.CLASS_NAME,value=self.qty_class).get_attribute("value");
        unit_price = self.driver.find_elements(by=By.CLASS_NAME,value=self.unit_price_class)[9].text
        return qty_count,unit_price,total_price,shipping_price,total_price_without_taxes

    def proceed_to_checkout(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.CLASS_NAME,value=self.proceed_to_checkout_class).click()

    def get_website_title(self):
        self.driver.implicitly_wait(5)
        return self.driver.title
