from selenium.webdriver.common.by import By
import time

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.signin_btn_classname = 'login'
        self.table_id = 'homefeatured'
        self.tab_women_name='Women'
        self.search_box_id='search_query_top'
        self.submit_search_name = 'submit_search'

    def click_signin_btn(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.CLASS_NAME, value=self.signin_btn_classname).click()


    def search_in_home_page_table(self,item_name):
        self.driver.implicitly_wait(5)
        x = self.driver.find_element(by=By.ID, value=self.table_id)
        element = 0
        for cell in x.find_elements(by=By.TAG_NAME, value='a'):
            if (cell.text == item_name):
                element = cell
                break
        if element != 0:
            #element.click()
            return item_name + " Found"
        else:
            return item_name + " Not found"

    def search_and_click_on_item(self,item_name):
        self.driver.implicitly_wait(5)
        x = self.driver.find_element(by=By.ID, value=self.table_id)
        element = 0
        for cell in x.find_elements(by=By.TAG_NAME, value='a'):
            if (cell.text == item_name):
                element = cell
                break
        if element != 0:
            element.click()


    def go_to_tab_women(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.LINK_TEXT,value=self.tab_women_name).click()

    def search_in_searchbox(self,text):
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.ID,value=self.search_box_id).send_keys(text)
        self.driver.find_element(by=By.NAME,value=self.submit_search_name).click()