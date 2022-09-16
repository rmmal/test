from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

class AddressPage():

    def __init__(self, driver):
        self.driver = driver
        self.address_id='address1'
        self.city_id =  'city'
        self.country_id ='id_country'
        self.state_id = 'id_state'
        self.zip_code_id = 'postcode'
        self.phone_id = 'phone'
        self.address_alias_id = 'alias'
        self.save_btn_id = 'submitAddress'
        self.procceed_btn_name = 'processAddress'
        self.new_address_class = 'address_address1'

    def fill_form(self,address,city,state,zip_code,phone,alias):
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.ID, value=self.address_id).send_keys(address)
        self.driver.find_element(by=By.ID, value=self.city_id).send_keys(city)
        select = Select(self.driver.find_element(by=By.ID, value=self.state_id))
        for option in select.options:
            value = option.text
            if value == state:
                option.click()
                break
        self.driver.find_element(by=By.ID, value=self.zip_code_id).send_keys(zip_code)
        self.driver.find_element(by=By.ID, value=self.phone_id).send_keys(phone)
        self.driver.find_element(by=By.ID, value=self.address_alias_id).send_keys(alias)
        self.driver.find_element(by=By.ID, value=self.save_btn_id).click()

    def get_website_title(self):
        self.driver.implicitly_wait(5)
        return self.driver.title

    def proceed_checkout(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.NAME,value=self.procceed_btn_name).click()

    def get_address(self):
        self.driver.implicitly_wait(5)
        return self.driver.find_elements(by=By.CLASS_NAME,value=self.new_address_class)[0].text