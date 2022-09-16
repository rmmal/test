from selenium.webdriver.common.by import By
from Pages.MyAccountPage import MyAccountsPage
import time

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.email_id='email'
        self.password_id='passwd'
        self.login_btn_id='SubmitLogin'

        self.reg_email_id = 'email_create'
        self.create_acc_btn_id='SubmitCreate'

        self.error_xpath = '//*[@id="center_column"]/div[1]/ol/li'

    def login_using_username_password(self,username,password):
        self.driver.implicitly_wait(5)

        #enter the username
        self.driver.find_element(by=By.ID,value=self.email_id).send_keys(username)

        #enter the password
        self.driver.find_element(by=By.ID, value=self.password_id).send_keys(password)

        #press login
        self.driver.find_element(by=By.ID,value=self.login_btn_id).click()


    def go_to_register_page(self,email):
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.ID,value=self.reg_email_id).send_keys(email)
        self.driver.find_element(by=By.ID,value=self.create_acc_btn_id).click()

    def go_to_login_page(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.LINK_TEXT, value=self.login_page_redirection_btn_name).click();

    def get_error(self):
        self.driver.implicitly_wait(5)
        return self.driver.find_element(by=By.XPATH,value=self.error_xpath).text
