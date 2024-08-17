from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_feed_page_locators import Locators


class OrderFeedPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_any_order_to_be_visible(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(Locators.ANY_ORDER))

    def click_on_order(self):
        self.driver.find_element(*Locators.ANY_ORDER).click()

    def wait_order_pop_up_window_is_displayed(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(Locators.ORDER_FEED_POP_UP_OF_ORDER))

    def get_all_orders_texts(self):
        order_elements = self.driver.find_elements(*Locators.ORDERS_LIST)
        return [order_element.text for order_element in order_elements]
    def wait_for_orders_to_be_visible(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_all_elements_located(Locators.ORDERS_LIST))

    def get_number_of_orders_for_all_time(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(Locators.TOTAL_COMPLETED_ORDERS_COUNTER))
        return self.driver.find_element(*Locators.TOTAL_COMPLETED_ORDERS_COUNTER).text

    def get_number_of_orders_for_today(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(Locators.COMPLETED_ORDERS_FOR_TODAY_COUNTER))
        return self.driver.find_element(*Locators.COMPLETED_ORDERS_FOR_TODAY_COUNTER).text

    def wait_for_orders_in_progress_to_be_visible(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_all_elements_located(Locators.ORDERS_IN_PROGRESS_LIST))

    def get_all_orders_in_progress_texts(self):
        order_elements = self.driver.find_elements(*Locators.ORDERS_IN_PROGRESS_LIST)
        return [order_element.text for order_element in order_elements]