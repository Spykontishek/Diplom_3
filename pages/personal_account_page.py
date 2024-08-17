from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants


class PersAcPage:
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    def __init__(self, driver):
        self.driver = driver

    def click_order_history_button(self):
        self.driver.find_element(*self.ORDER_HISTORY_BUTTON).click()

    def click_order_history_button_java(self):
        element = self.driver.find_element(*self.ORDER_HISTORY_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_go_to_order_history_url(self):
        WebDriverWait(self.driver, 3).until(EC.url_to_be(Constants.ORDER_HISTORY_URL))

    def click_exit_button(self):
        self.driver.find_element(*self.EXIT_BUTTON).click()

    def wait_go_to_auth_url(self):
        WebDriverWait(self.driver, 3).until(EC.url_to_be(Constants.AUTH_URL))

    def wait_order_history_button_is_clickable(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.ORDER_HISTORY_BUTTON))