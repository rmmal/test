from selenium.webdriver.common.by import By
import time

class ShippingPage():

    def __init__(self, driver):
        self.driver = driver
        self.header_class = 'page-heading'
        self.proceed_btn_name = 'processCarrier'
        self.agree_terms_conditions_id = 'cgv'

    def proceed_to_checkout(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.ID,value=self.agree_terms_conditions_id).click()
        self.driver.find_element(by=By.NAME,value=self.proceed_btn_name).click()

    def get_header_text(self):
        self.driver.implicitly_wait(5)
        return self.driver.find_element(by=By.CLASS_NAME,value=self.header_class).text
