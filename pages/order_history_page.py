from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderHistoryPage:
    ORDER_CONFIRMATION_WINDOW = (By.XPATH, "//p[@class = 'text text_type_digits-default']")

    def __init__(self, driver):
        self.driver = driver

    def get_number_of_order(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.ORDER_CONFIRMATION_WINDOW))
        return self.driver.find_element(*self.ORDER_CONFIRMATION_WINDOW).text




