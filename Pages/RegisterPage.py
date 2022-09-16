import time

from selenium.webdriver.common.by import By
from Pages.MyAccountPage import MyAccountsPage
class RegisterPage():

    def __init__(self,driver):
        self.driver = driver
        self.gender_id = 'id_gender1'
        self.firstname_id = 'customer_firstname'
        self.Lastname_id= 'customer_lastname'
        self.Password_id = 'passwd'
        self.register_btn_id = 'submitAccount'


    def register(self,Firstname,Lastname,password):
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.ID, value=self.gender_id).click()
        self.driver.find_element(by=By.ID, value=self.firstname_id).send_keys(Firstname)
        self.driver.find_element(by=By.ID, value=self.Lastname_id).send_keys(Lastname)
        self.driver.find_element(by=By.ID, value=self.Password_id).send_keys(password)
        self.driver.find_element(by=By.ID,value=self.register_btn_id).click()
