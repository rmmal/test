from selenium.webdriver.common.by import By
import time

class PaymentPage():

    def __init__(self, driver):
        self.driver = driver
        self.header_class = 'page-heading'
        self.bank_wire_class = 'bankwire'

        self.final_qty_class = 'cart_quantity'
        self.final_unit_price_class = 'price'
        self.final_shipping_class = 'price'
        self.final_total_ship_tax_id = 'total_price'
        self.confirm_order_class = 'button-medium'
        self.success_class = 'alert-success'

    def pay_by_bank_wire(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.CLASS_NAME,value=self.bank_wire_class).click()

    def get_header_text(self):
        self.driver.implicitly_wait(5)
        return self.driver.find_element(by=By.CLASS_NAME,value=self.header_class).text

    def get_final_prices(self):
        self.driver.implicitly_wait(5)
        final_qty = self.driver.find_elements(by=By.CLASS_NAME, value=self.final_qty_class)[1].text
        final_unit_price = self.driver.find_elements(by=By.CLASS_NAME, value=self.final_unit_price_class)[10].text
        final_shipping = self.driver.find_elements(by=By.CLASS_NAME, value=self.final_shipping_class)[5].text
        final_total_ship_tax= self.driver.find_element(by=By.ID, value=self.final_total_ship_tax_id).text

        return final_qty,final_unit_price,final_shipping,final_total_ship_tax

    def confirm_order(self):
        self.driver.implicitly_wait(5)
        self.driver.find_elements(by=By.CLASS_NAME, value=self.confirm_order_class)[1].click()

    def get_success_message(self):
        self.driver.implicitly_wait(5)
        time.sleep(5)
        return self.driver.find_element(by=By.CLASS_NAME,value=self.success_class).text