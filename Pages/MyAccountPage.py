from selenium.webdriver.common.by import By


class MyAccountsPage():
    def __init__(self,driver):
        self.driver = driver
        self.signout_class = 'logout'
        self.home_logo_text = 'Home'

    def signout(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.CLASS_NAME,value=self.signout_class).click()

    def go_to_homepage(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.LINK_TEXT,value=self.home_logo_text).click()

    def get_website_title(self):
        self.driver.implicitly_wait(5)
        return self.driver.title