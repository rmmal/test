from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

class ProductPage():

    def __init__(self, driver):
        self.driver = driver
        self.size_group_id = 'group_1'
        self.white_color_id = 'color_8'
        self.black_color_id = 'color_11'
        self.increase_product_count_classname ='product_quantity_up'
        self.add_to_cart_name ='Submit'
        self.proceed_to_checkout='Proceed to checkout'

    def Add_to_cart(self,quantity,size,color):
        self.driver.implicitly_wait(5)
        # Increase count
        for count in range(quantity - 1):
            self.driver.find_element(by=By.CLASS_NAME, value=self.increase_product_count_classname).click()

        # Select Size
        self.driver.implicitly_wait(5)
        options= self.driver.find_element(by=By.ID, value=self.size_group_id)
        for option in options.find_elements_by_tag_name('option'):
            if option.text == size:
                option.click()  # select() in earlier versions of webdriver
                break

        # Select Color
        if color.lower() == 'white':
            self.driver.find_element(by=By.ID, value=self.white_color_id).click()
        elif color.lower() == 'black':
            self.driver.find_element(by=By.ID, value=self.black_color_id).click()

        # Press Add to cart
        self.driver.find_element(by=By.NAME, value=self.add_to_cart_name).click()

        # Press proceed to checkout
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.LINK_TEXT, value=self.proceed_to_checkout).click()


