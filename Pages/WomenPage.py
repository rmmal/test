from selenium.webdriver.common.by import By
import time

class WomenPage():

    def __init__(self, driver):
        self.driver = driver
        self.table_id = 'product_list'


    def search_in_women_page_table(self,item_name):
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
